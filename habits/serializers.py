from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        validate_habit(data)
        return data

    class Meta:
        model = Habit
        fields = "__all__"


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'periodicity', 'action_time', 'is_nice')
