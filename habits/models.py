from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIODS = [
        ('1', 'каждый день'),
        ('2', 'раз в 2 дня'),
        ('3', 'раз в 3 дня'),
        ('4', 'раз в 4 дня'),
        ('5', 'раз в 5 дней'),
        ('6', 'раз в 6 дней'),
        ('7', 'раз в 7 дней'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=250, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=250, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='приятная привычка')
    nice_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.CharField(max_length=1, choices=PERIODS, default=1, verbose_name='периодичность')
    gift = models.CharField(max_length=250, verbose_name='вознаграждение', **NULLABLE)
    action_time = models.TimeField(max_length=120, verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публичная привычка')

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.time} в {self.place} {self.periodicity}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
