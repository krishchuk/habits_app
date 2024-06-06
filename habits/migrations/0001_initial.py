# Generated by Django 5.0.6 on 2024-06-06 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=250, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='приятная привычка')),
                ('periodicity', models.CharField(choices=[('1', 'каждый день'), ('2', 'раз в 2 дня'), ('3', 'раз в 3 дня'), ('4', 'раз в 4 дня'), ('5', 'раз в 5 дней'), ('6', 'раз в 6 дней'), ('7', 'раз в 7 дней')], default=1, max_length=1, verbose_name='периодичность')),
                ('gift', models.CharField(blank=True, max_length=250, null=True, verbose_name='вознаграждение')),
                ('action_time', models.TimeField(max_length=120, verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная привычка')),
                ('nice_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
