# FR_test_task

Целью проекта было создать сервис для управления рассылками,с отправкой сообщений на внешнее API

Для начала работы требуется:
-Создать и запустить базу данных Postgresql
-Запустить сервер redis
-Создать файл secret_data.py и записать в него:

  Имя созданной базы данных в NAME_DB
  Имя пользователя в USER_DB
  Пароль от базы данных в PASSWORD_DB, если есть, иначе значение должно быть равно ""
  Хоста сервера redis в REDIS_HOST
  Порт, на котором работает сервер redis в REDIS_PORT

  TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTA5NzQ3MjUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkdhcnJ5X25vdF90aGVfd2l6YXJkIn0.o5u8x1B4NXyloyFvT9mcEJF4v7fIn-8i-kZg6WMz78I'


-Перейти в папку, в которой располагается файл manage.py и выполнить следующие команды:

  python manage.py makemigrations

  python manage.py migrate


Для запуска приложения требуется открыть 2 терминала, перейти в них в папку с файлом manage.py и написать следующие команды:

  В первом: celery -A notification_service worker -l info -P gevent

  Во втором: python manage.py runserver


Стек используемых технологий:
-Язык программирования Python
-Фреймворк для создания веб-приложений Django
-Django REST API для работы с REST API
-Postgresql в качестве базы данных
-Celery для фонового выполнения задач
-Redis для работы с Celery
-Библиотека Python gevent для корректной работы Celery
-Swagger для описания реализованных методов в формате OpenAPI
-Django-filters для фильтрации данных
-Библиотека Python phone_field для хранения телефонных номеров

Описание структуры приложения:

-Всю основную информацию об API после запуска приложения можно найти перейдя по адресу:

  http://127.0.0.1:8000/swagger/

-Для получения всех сообщений в рассылке нужно перейти по адресу:

http://127.0.0.1:8000/mailer/distributions/{distribution_id}/messages

Где distribution_id - ID нужной рассылки
