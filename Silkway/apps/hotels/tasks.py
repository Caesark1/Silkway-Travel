from __future__ import unicode_literals
from Silkway.celery import app
from django.core.mail import send_mail
from django.conf import settings


@app.task
def send_userdata(user_data):
    mailfrom = settings.EMAIL_HOST_USER
    mailto = user_data['email']
    subject = "Заявка"
    message = f'''Имя: {user_data["first_name"]}
                Фамилия: {user_data["last_name"]}
                Mail: {user_data["email"]}
                Номер телефона: {user_data["phone_number"]}'''
    send_mail(subject,message ,mailfrom, [mailto], fail_silently=False)

