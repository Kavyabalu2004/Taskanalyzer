from django.db import models

# Create your models here.
# backend/tasks/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    estimated_hours = models.PositiveIntegerField()
    importance = models.PositiveIntegerField()  # Use a scale from 1 to 10
    dependencies = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.title
