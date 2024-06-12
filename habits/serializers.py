from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'periodicity', 'action_time', 'is_nice')
