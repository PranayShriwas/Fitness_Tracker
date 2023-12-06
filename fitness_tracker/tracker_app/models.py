# tracker_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()  # in minutes
    date = models.DateField()

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target_weight = models.FloatField()
