from django.urls import path
from . import views

app_name = 'datasets'

urlpatterns = [
    path('', views.dataset_list, name='list'),
    path('load-builtin/', views.load_builtin, name='load_builtin'),
    path('<int:pk>/', views.dataset_preview, name='preview'),
    path('<int:pk>/columns/', views.dataset_columns, name='columns'),
]