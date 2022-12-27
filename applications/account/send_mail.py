from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    send_mail(
        'Активация пользователя',
        full_link,
        'read87488@gmail.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'e352709@gmail.com',
        [email]
    )
