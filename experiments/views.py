from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import pickle
import os
import copy
import pandas as pd
import numpy as np
from .models import Experiment
from datasets.models import Dataset
from ml_engine.preprocessor import get_column_info, preprocess
from ml_engine.trainer import train
from ml_engine.evaluator import evaluate

def experiment_list(request):
    experiments = Experiment.objects.select_related('dataset').order_by('-created_at')
    return render(request, 'experiments/list.html', {'experiments': experiments})

def experiment_new(request):
    datasets = Dataset.objects.all().order_by('-uploaded_at')
    selected_dataset = request.GET.get('dataset', '')

    columns = []
    if selected_dataset:
        try:
            ds = Dataset.objects.get(pk=selected_dataset)
            df = pd.read_csv(ds.file.path)
            columns = [col for col in df.columns]
        except Exception:
            pass

    if request.method == 'POST':
        dataset_id = request.POST.get('dataset_id')
        target_column = request.POST.get('target_column')
        problem_type = request.POST.get('problem_type')
        algorithm = request.POST.get('algorithm')
        raw_test_size = request.POST.get('test_size', '20')
        randomize_split = request.POST.get('randomize_split') == 'on'
        use_automl = request.POST.get('use_automl') == 'on'
        
        try:
            parsed_test_size = float(raw_test_size)
        except (TypeError, ValueError):
            parsed_test_size = 20.0

        test_size = parsed_test_size / 100 if parsed_test_size > 1 else parsed_test_size

        if test_size <= 0 or test_size >= 1:
            test_size = 0.2
        
        random_state = None if randomize_split else 42

        if not all([dataset_id, target_column, problem_type]):
            messages.error(request, 'يرجى ملء جميع الحقول')
            return redirect('experiments:new')
        
        if not use_automl and not algorithm:
            messages.error(request, 'يرجى اختيار خوارزمية أو تفعيل AutoML')
            return redirect('experiments:new')

        try:
            dataset = Dataset.objects.get(pk=dataset_id)
            df = pd.read_csv(dataset.file.path)
            
            scale_features = algorithm in ['knn', 'logistic_regression'] if not use_automl else True
            
            X_train, X_test, y_train, y_test, encoders, scaler, feature_names = preprocess(
                df, target_column, test_size=test_size, 
                random_state=random_state, scale_features=scale_features
            )
            
            if use_automl:
                from ml_engine.automl import run_automl
                automl_result = run_automl(X_train, X_test, y_train, y_test, problem_type)
                model = automl_result['best_model']
                algorithm = automl_result['best_algorithm']
                # Break shared references between best_result and all_results entries
                # to avoid JSON circular reference during Experiment save.
                result = copy.deepcopy(automl_result['best_result'])
                result['automl_results'] = copy.deepcopy(automl_result['all_results'])
            else:
                model = train(X_train, y_train, algorithm, problem_type)
                result = evaluate(model, X_test, y_test, problem_type)

            if problem_type == 'regression':
                diffs = [round(abs(a - p), 2) for a, p in zip(result['actual'], result['predictions'])]
                result['diffs'] = diffs

            model_bytes = pickle.dumps({
                'model': model,
                'encoders': encoders,
                'scaler': scaler,
                'feature_names': feature_names,
                'problem_type': problem_type
            })

            accuracy_val = result.get('accuracy', 0)
            r2_val = result.get('r2', 0)

            exp = Experiment.objects.create(
                dataset=dataset,
                problem_type=problem_type,
                algorithm='automl' if use_automl else algorithm,
                target_column=target_column,
                test_size=test_size,
                random_state=random_state,
                accuracy=accuracy_val if problem_type == 'classification' else None,
                r2_score=r2_val if problem_type == 'regression' else None,
                result_json={
                    **result, 
                    'feature_names': feature_names,
                    'original_features': encoders.get('original_features', []),
                    'test_size': test_size,
                    'random_state': random_state,
                    'scaled': scale_features
                }
            )

            model_path = f'media/models/exp_{exp.id}.pkl'
            os.makedirs('media/models', exist_ok=True)
            with open(model_path, 'wb') as f:
                pickle.dump({
                    'model': model,
                    'encoders': encoders,
                    'scaler': scaler,
                    'feature_names': feature_names,
                    'problem_type': problem_type
                }, f)

            return redirect('experiments:detail', pk=exp.id)

        except Exception as e:
            messages.error(request, f'خطأ في التدريب: {str(e)}')
            return redirect('experiments:new')

    return render(request, 'experiments/new.html', {
        'datasets': datasets,
        'selected_dataset': selected_dataset,
        'columns': columns,
    })

def experiment_detail(request, pk):
    exp = get_object_or_404(Experiment, pk=pk)
    result = exp.result_json or {}
    feature_names = result.get('feature_names', [])
    feature_inputs = []

    try:
        df = pd.read_csv(exp.dataset.file.path)
        source_columns = get_column_info(df)
        source_map = {col['name']: col for col in source_columns}
        original_features = result.get('original_features') or result.get('encoders', {}).get('original_features') or feature_names

        for feat in original_features:
            col_info = source_map.get(feat, {})
            feature_inputs.append({
                'name': feat,
                'type': col_info.get('type', 'numeric'),
            })
    except Exception:
        feature_inputs = [{'name': feat, 'type': 'numeric'} for feat in feature_names]
    
    report = result.get('classification_report')
    if isinstance(report, dict) and 'weighted avg' in report and 'weighted_avg' not in report:
        report['weighted_avg'] = report['weighted avg']
    if isinstance(report, dict):
        weighted_avg = report.get('weighted_avg')
        if isinstance(weighted_avg, dict) and 'f1-score' in weighted_avg and 'f1_score' not in weighted_avg:
            weighted_avg['f1_score'] = weighted_avg['f1-score']

    zipped_results = list(zip(
        result.get('actual', []),
        result.get('predictions', []),
        result.get('diffs', []),
    ))
    
    automl_results = result.get('automl_results', [])
    algo_labels = {
        'linear_regression': 'Linear Regression',
        'logistic_regression': 'Logistic Regression',
        'decision_tree': 'Decision Tree',
        'knn': 'KNN',
    }
    for item in automl_results:
        item['label'] = algo_labels.get(item.get('algorithm'), item.get('algorithm'))
    best_automl = None
    if exp.algorithm == 'automl' and automl_results:
        best_automl = max(automl_results, key=lambda x: x.get('score', float('-inf')))

    ALGO_CHOICES = {
        'regression': [
            {'value': 'linear_regression', 'label': 'Linear Regression'},
            {'value': 'decision_tree', 'label': 'Decision Tree'},
            {'value': 'knn', 'label': 'KNN'},
        ],
        'classification': [
            {'value': 'logistic_regression', 'label': 'Logistic Regression'},
            {'value': 'decision_tree', 'label': 'Decision Tree'},
            {'value': 'knn', 'label': 'KNN'},
        ],
    }
    other_algos = [a for a in ALGO_CHOICES.get(exp.problem_type, []) if a['value'] != exp.algorithm]

    return render(request, 'experiments/detail.html', {
        'experiment': exp,
        'result': result,
        'features': feature_names,
        'feature_inputs': feature_inputs,
        'other_algos': other_algos,
        'zipped_results': zipped_results,
        'automl_results': automl_results,
        'best_automl': best_automl,
    })

def experiment_automl_report(request, pk):
    exp = get_object_or_404(Experiment, pk=pk)
    result = exp.result_json or {}
    automl_results = result.get('automl_results', [])

    if exp.algorithm != 'automl' or not automl_results:
        messages.info(request, 'لا توجد نتائج AutoML لهذه التجربة.')
        return redirect('experiments:detail', pk=pk)

    sorted_results = sorted(
        automl_results,
        key=lambda x: x.get('score', float('-inf')),
        reverse=True
    )
    best = sorted_results[0]

    algo_labels = {
        'linear_regression': 'Linear Regression',
        'logistic_regression': 'Logistic Regression',
        'decision_tree': 'Decision Tree',
        'knn': 'KNN',
    }

    for item in sorted_results:
        item['label'] = algo_labels.get(item.get('algorithm'), item.get('algorithm'))

    return render(request, 'experiments/automl_report.html', {
        'experiment': exp,
        'automl_results': sorted_results,
        'best_automl': best,
        'score_label': 'Accuracy' if exp.problem_type == 'classification' else 'R²',
    })

@require_POST
def experiment_predict(request, pk):
    exp = get_object_or_404(Experiment, pk=pk)
    try:
        model_path = f'media/models/exp_{pk}.pkl'
        with open(model_path, 'rb') as f:
            saved = pickle.load(f)

        model = saved['model']
        encoders = saved.get('encoders', {})
        features = saved.get('feature_names') or saved.get('features', [])
        categorical_cols = set(encoders.get('categorical_cols', []))
        original_features = encoders.get('original_features', [])
        scaler = saved.get('scaler')

        body = json.loads(request.body)
        if original_features:
            input_row = {}
            for feat in original_features:
                val = body.get(feat, '')
                if feat in categorical_cols:
                    input_row[feat] = str(val).strip()
                else:
                    try:
                        input_row[feat] = float(val)
                    except (TypeError, ValueError):
                        input_row[feat] = 0.0

            input_df = pd.DataFrame([input_row])
            if categorical_cols:
                input_df = pd.get_dummies(input_df, columns=list(categorical_cols), drop_first=True)
            input_df = input_df.reindex(columns=features, fill_value=0)
            row = input_df.values
        else:
            row = []
            for feat in features:
                val = body.get(feat, 0)
                try:
                    row.append(float(val))
                except (TypeError, ValueError):
                    row.append(0.0)
            row = [row]

        if scaler is not None:
            row = scaler.transform(row)

        prediction = model.predict(row)[0]
        if isinstance(prediction, (np.floating, float)):
            prediction = round(float(prediction), 2)
        else:
            prediction = str(prediction)

        return JsonResponse({'prediction': prediction})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
