import unittest
from datetime import datetime
from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from config.telegram_bot import send_telegram_message, TELEGRAM_TOKEN
from habits.models import Habit
from habits.tasks import TELEGRAM_CHAT_ID
from users.models import User


class TestTelegramBot(unittest.TestCase):
    @patch('config.telegram_bot.requests.post')
    def test_send_telegram_message(self, mock_post):
        mock_post.return_value.json.return_value = {'ok': True}

        chat_id = TELEGRAM_CHAT_ID
        message_text = 'Тестовое сообщение'
        response = send_telegram_message(chat_id, message_text)

        mock_post.assert_called_once_with(
            'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN),
            json={'chat_id': chat_id, 'text': message_text}
        )

        self.assertEqual(response, {'ok': True})


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='admin@sky.pro')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(user=self.user, place='place', time=datetime.now().time(), action='action',
                                          gift='gift', action_time=120)
        self.nice_habit = Habit.objects.create(user=self.user, place='nice_place', time=datetime.now().time(),
                                               action='nice_action', is_nice=True, action_time=60)

    def test_create_habit(self):
        data = {
            'user': self.user.id,
            'place': 'place test',
            'time': datetime.now().time(),
            'action': 'action test',
            'is_nice': False,
            'periodicity': '2',
            'gift': 'gift test',
            'action_time': 120,
            'is_public': True
            }
        response = self.client.post('habits/create/', data=data, format='json')
        print(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(place=data['place']).exists())

    def test_retrieve_habit(self):
        path = reverse('habits:habit_detail', args=[self.habit.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_retrieve_not_existent_habit(self):
        not_existent_habit_id = 9999
        path = reverse('habits:habit_detail', args=[not_existent_habit_id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_habit(self):
        path = reverse('habits:habit_update', args=[self.habit.id])
        data = {'place': 'new place', 'gift': 'new gift'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, data['place'])

    def test_delete_habit(self):
        not_owner = User.objects.create(id=3, email='moderator@test.ru',
                                        password='12345')
        self.client.force_authenticate(user=not_owner)
        path = reverse('habits:habit_delete', [self.habit.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
