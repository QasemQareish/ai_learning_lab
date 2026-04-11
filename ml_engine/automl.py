from .trainer import get_model, train
from .evaluator import evaluate
import numpy as np

def run_automl(X_train, X_test, y_train, y_test, problem_type):
    """
    Try multiple algorithms and return the best one.
    
    Returns:
        dict with best_model, best_algorithm, best_score, all_results
    """
    
    if problem_type == 'classification':
        algorithms = ['logistic_regression', 'decision_tree', 'knn']
        score_key = 'accuracy'
    else:
        algorithms = ['linear_regression', 'decision_tree', 'knn']
        score_key = 'r2'
    
    results = []
    best_score = -np.inf
    best_model = None
    best_algorithm = None
    best_result = None
    
    for algo in algorithms:
        try:
            model = train(X_train, y_train, algo, problem_type)
            result = evaluate(model, X_test, y_test, problem_type)
            
            score = result.get(score_key, 0)
            
            results.append({
                'algorithm': algo,
                'score': score,
                'result': result
            })
            
            if score > best_score:
                best_score = score
                best_model = model
                best_algorithm = algo
                best_result = result
                
        except Exception as e:
            print(f"Error with {algo}: {str(e)}")
            continue
    
    return {
        'best_model': best_model,
        'best_algorithm': best_algorithm,
        'best_score': best_score,
        'best_result': best_result,
        'all_results': results
    }