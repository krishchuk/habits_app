from django.urls import path

from habits.views import (HabitListAPIView, HabitDetailAPIView, HabitCreateAPIView, HabitUpdateAPIView,
                          HabitDeleteAPIView, HabitPublicListAPIView)

app_name = "habits"

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habit_list"),
    path("habits/public/", HabitPublicListAPIView.as_view(), name="habit_public"),
    path("habits/<int:pk>/", HabitDetailAPIView.as_view(), name="habit_detail"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/<int:pk>/delete/", HabitDeleteAPIView.as_view(), name="habit_delete"),
]
