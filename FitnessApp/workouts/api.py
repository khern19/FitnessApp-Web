from workouts.models import Workouts
from rest_framework import viewsets, permissions
from .serializers import WorkoutSerializer

# Workout viewset


class WorkoutViewSet(viewset.ModelViewSet):
    queryset = Workouts.objects.all()
