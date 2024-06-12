from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitPublicSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitPublicSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = CustomPagination
    permission_classes = [AllowAny]


class HabitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        else:
            return Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
