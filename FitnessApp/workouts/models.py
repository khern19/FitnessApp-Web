from django.db import models


class Workouts(models.Model):
    workout_name = models.CharField(max_length=150)
    reps = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    distance = models.DecimalField(max_digits=9, decimal_places=6)
    time = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField(blank=True, null=True)
