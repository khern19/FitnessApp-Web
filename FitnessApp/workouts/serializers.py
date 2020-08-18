from rest_framework import serializers
from workouts.models import Workouts

# Workout serializer


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workouts
        fields = '__all__'
