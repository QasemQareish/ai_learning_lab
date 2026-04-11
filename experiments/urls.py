from django.urls import path
from . import views

app_name = 'experiments'

urlpatterns = [
    path('', views.experiment_list, name='list'),
    path('new/', views.experiment_new, name='new'),
    path('<int:pk>/', views.experiment_detail, name='detail'),
    path('<int:pk>/automl-report/', views.experiment_automl_report, name='automl_report'),
    path('<int:pk>/predict/', views.experiment_predict, name='predict'),
]
