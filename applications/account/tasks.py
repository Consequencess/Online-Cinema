from django.core.mail import send_mail

from config.celery import app


@app.task
def spam_message():
    full_link = f'http://localhost:8000/api/v1/movie/'
    send_mail(
        'Привет новые товары пришли можешь глануть',
        full_link,
        'read87488@gmail.com',
        ['read87488@gmail.com']

    )