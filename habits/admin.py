from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class AdminUser(admin.ModelAdmin):
    list_display = (
        "user",
        "place",
        "time",
        "action",
        "is_nice",
        "nice_habit",
        "periodicity",
        "gift",
        "action_time",
        "is_public",
    )
