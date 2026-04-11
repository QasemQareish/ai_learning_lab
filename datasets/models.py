from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    row_count = models.IntegerField(default=0)
    column_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name