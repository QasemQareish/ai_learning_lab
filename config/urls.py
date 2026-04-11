from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from datasets.models import Dataset
from experiments.models import Experiment

def home(request):
    pipeline_steps = [
        {'icon': '📂', 'title': 'ارفع البيانات', 'desc': 'CSV أو dataset جاهز'},
        {'icon': '🔍', 'title': 'استكشف', 'desc': 'شوف الأعمدة والأنواع'},
        {'icon': '⚙️', 'title': 'اختر الموديل', 'desc': 'Regression أو Classification'},
        {'icon': '⚡', 'title': 'درّب', 'desc': 'بضغطة زر واحدة'},
        {'icon': '📊', 'title': 'النتائج', 'desc': 'Accuracy + Confusion Matrix'},
    ]
    return render(request, 'home.html', {
        'datasets_count': Dataset.objects.count(),
        'experiments_count': Experiment.objects.count(),
        'recent_experiments': Experiment.objects.select_related('dataset').order_by('-created_at')[:5],
        'pipeline_steps': pipeline_steps,
    })

def learn_center(request):
    return render(request, 'learn/index.html')

def learn_code_lab(request):
    return render(request, 'learn/code_lab.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('learn/', learn_center, name='learn_center'),
    path('learn/code-lab/', learn_code_lab, name='learn_code_lab'),
    path('datasets/', include('datasets.urls')),
    path('experiments/', include('experiments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)