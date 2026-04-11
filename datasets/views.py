from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Dataset
from ml_engine.preprocessor import get_column_info
import pandas as pd
import io
from pathlib import Path
from django.core.files.base import ContentFile

BUILTIN_DATASETS = [
    {
        'key': 'student',
        'name': 'Student Performance',
        'icon': '🎓',
        'desc': 'بيانات أداء الطلاب — تنبأ بالدرجات',
        'rows': 150,
        'file': 'student.csv',
    },
    {
        'key': 'iris',
        'name': 'Iris Flowers',
        'icon': '🌸',
        'desc': 'تصنيف أنواع الزهور الكلاسيكي',
        'rows': 150,
        'file': 'iris.csv',
    },
    {
        'key': 'titanic',
        'name': 'Titanic Survival',
        'icon': '🚢',
        'desc': 'توقع من نجا من كارثة تايتانيك',
        'rows': 891,
        'file': 'titanic.csv',
    },
]

BUILTIN_DATA_DIR = Path(__file__).resolve().parent.parent / 'datasets' / 'builtin_data'

def get_builtin_df(key):
    meta = next((d for d in BUILTIN_DATASETS if d['key'] == key), None)
    if not meta:
        return None
    csv_path = BUILTIN_DATA_DIR / meta['file']
    if not csv_path.exists():
        return None
    return pd.read_csv(csv_path)

def dataset_list(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        file = request.FILES.get('file')
        if not name or not file:
            messages.error(request, 'يرجى إدخال الاسم وتحديد الملف')
            return redirect('datasets:list')
        try:
            df = pd.read_csv(file)
            dataset = Dataset.objects.create(
                name=name,
                file=file,
                row_count=len(df),
                column_count=len(df.columns)
            )
            messages.success(request, f'تم رفع "{name}" بنجاح — {len(df)} صف')
            return redirect('datasets:preview', pk=dataset.id)
        except Exception as e:
            messages.error(request, f'خطأ في قراءة الملف: {str(e)}')
            return redirect('datasets:list')

    datasets = Dataset.objects.all().order_by('-uploaded_at')
    return render(request, 'datasets/list.html', {
        'datasets': datasets,
        'builtin_datasets': BUILTIN_DATASETS,
    })

def load_builtin(request):
    if request.method == 'POST':
        key = request.POST.get('dataset_key')
        meta = next((d for d in BUILTIN_DATASETS if d['key'] == key), None)
        if not meta:
            messages.error(request, 'Dataset غير موجود')
            return redirect('datasets:list')

        existing = Dataset.objects.filter(name=meta['name']).first()
        if existing:
            return redirect('datasets:preview', pk=existing.id)

        df = get_builtin_df(key)
        if df is None:
            messages.error(request, 'خطأ في تحميل البيانات')
            return redirect('datasets:list')

        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        file_content = ContentFile(csv_buffer.getvalue().encode('utf-8'))

        dataset = Dataset(name=meta['name'], row_count=len(df), column_count=len(df.columns))
        dataset.file.save(f"{key}.csv", file_content)
        dataset.save()

        messages.success(request, f'تم تحميل "{meta["name"]}" بنجاح')
        return redirect('datasets:preview', pk=dataset.id)
    return redirect('datasets:list')

def dataset_preview(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    try:
        df = pd.read_csv(dataset.file.path)
        columns = get_column_info(df)
        preview_rows = [list(row) for row in df.head(10).values]
        preview_columns = list(df.columns)
    except Exception:
        columns, preview_rows, preview_columns = [], [], []

    return render(request, 'datasets/preview.html', {
        'dataset': dataset,
        'columns': columns,
        'preview_rows': preview_rows,
        'preview_columns': preview_columns,
    })

def dataset_columns(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    try:
        df = pd.read_csv(dataset.file.path)
        columns = get_column_info(df)
        return JsonResponse({'columns': columns})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)