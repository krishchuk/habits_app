# Трекер полезных привычек

## Описание проекта

Приложение "Трекер полезных привычек" вдохновлено книгой "Атомные привычки" Джеймса Клира.
Цель приложения - помочь пользователям приобрести новые полезные привычки и избавиться от старых плохих привычек.

## Запуск проекта с Docker

#### Настройте переменные окружения в файле `.env` по примеру из `.env.sample`:

```
SECRET_KEY=your-secret-key
...
TELEGRAM_TOKEN=your-telegram-token
```

#### Создание образа из Dockerfile: 
```bash
docker-compose build
```

#### Запуск контейнера: 
```bash
docker-compose up
```

или

#### Создание образа с запуском контейнера: 
```bash
docker-compose up --build
```

или

#### Создание образа с запуском контейнера в фоновом режиме: 
```bash
docker-compose up -d --build
```


## Установка и запуск БЕЗ использования Docker

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/krishchuk/habits_app.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Настройте переменные окружения в файле `.env` по примеру из `.env.sample`:

    ```
    SECRET_KEY=your-secret-key
    ...
    TELEGRAM_TOKEN=your-telegram-token
    ```

4. Выполните миграции:

    ```bash
    python manage.py migrate
    ```

5. Запустите Celery для выполнения отложенных задач:

    для Linux / macOS:

    ```bash
    celery -A config worker -l INFO
    ```
   для Windows:
   
    ```bash
    celery -A config worker -l INFO -P eventlet
    ```

6. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

7. Приложение доступно по адресу http://127.0.0.1:8000/.