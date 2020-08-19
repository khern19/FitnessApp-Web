from workouts.models import Workouts
from rest_framework import viewsets, permissions
from .serializers import WorkoutSerializer

# Workout viewset


class WorkoutViewSet(viewsets.ModelViewSet):
    # queryset = Workouts.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = WorkoutSerializer
