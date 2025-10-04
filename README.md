# Django Shop Project

Простое учебное Django-приложение интернет-магазина, реализованное с использованием PostgreSQL, моделей, админ-панели, ORM-запросов, фикстур и кастомной команды.

В проекте реализованы:
- Модели `Product` и `Category` с описанием и связями.
- Поддержка изображений товаров (медиафайлы).
- Админка с настройкой отображения, фильтрацией, поиском и предпросмотром изображений.
- Импорт данных через фикстуры.
- Кастомная команда загрузки тестовых данных.

## Стек

- Python 3.11+
- Django 5.x
- PostgreSQL
- Poetry
- Bootstrap (вёрстка)

## Запуск проекта

Клонируйте репо:
```
git clone https://github.com/GuyMonagan/django-shop-project
```

Перейдите в папку проекта:
```
cd django-shop-project/src
```
Установите зависимости:
```
poetry install
```
Создайте и настройте .env файл:

```
DB_NAME=shop_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

```
Примените миграции:
```
poetry run python manage.py migrate
```
Создайте суперпользвателя:

```
poetry run python manage.py createsuperuser
```
Запустите сервер:
```
poetry run python manage.py runserver
```

Убедитесь, что создана фикстура по пути:

```
catalog/fixtures/initial_data.json
```

Выполните кастомную команду:

```commandline
poetry run python manage.py load_test_data
```

## Лицензия

Учебный проект. Используется в рамках курса Skypro Python-разработчик
