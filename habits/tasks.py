from celery import shared_task
from django.utils import timezone

from config.telegram_bot import send_telegram_message
from .models import Habit


@shared_task
def send_habit_notifications():
    current_habits = Habit.objects.filter(time__lte=timezone.now())
    for habit in current_habits:
        send_notification.delay(habit.id)


@shared_task
def send_notification(habit_id):
    habit = Habit.objects.get(id=habit_id)
    chat_id = f'@{habit.user.tg_nick}'
    text = f"Не забудьте выполнить привычку: {habit.action}"
    send_telegram_message(chat_id, text)
