from django.db import models
from datasets.models import Dataset

class Experiment(models.Model):
    ALGORITHM_CHOICES = [
        ('linear_regression', 'Linear Regression'),
        ('logistic_regression', 'Logistic Regression'),
        ('decision_tree', 'Decision Tree'),
        ('knn', 'KNN'),
        ('automl', 'AutoML (Best Model)'),
    ]

    PROBLEM_CHOICES = [
        ('regression', 'Regression'),
        ('classification', 'Classification'),
    ]

    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    problem_type = models.CharField(max_length=20, choices=PROBLEM_CHOICES)
    algorithm = models.CharField(max_length=30, choices=ALGORITHM_CHOICES)
    target_column = models.CharField(max_length=100)
    test_size = models.FloatField(default=0.2)
    random_state = models.IntegerField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    r2_score = models.FloatField(null=True, blank=True)
    result_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.algorithm} on {self.dataset.name}"
    
    def get_primary_score(self):
        """Return the primary metric based on problem type"""
        if self.problem_type == 'classification':
            return self.accuracy
        else:
            return self.r2_score