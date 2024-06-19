from celery import shared_task
from django.utils import timezone
import requests

from config.telegram_bot import send_telegram_message, TELEGRAM_TOKEN
from habits.models import Habit


@shared_task
def send_habit_notifications():
    current_habits = Habit.objects.filter(time__lte=timezone.now())
    for habit in current_habits:
        send_notification.delay(habit.id)


@shared_task
def send_notification(habit_id):
    habit = Habit.objects.get(id=habit_id)

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    request = requests.get(url).json()
    print(request)
    chat_id = request['result'][0]['message']['chat']['id']
    print(chat_id)

    text = f"Не забудьте выполнить привычку: {habit.action}"
    send_telegram_message(chat_id, text)
