# tasks.py
from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import datetime
from .views import send_account_summary_email

@shared_task
def send_account_summary_emails():
    User = get_user_model()
    now = datetime.now()
    year = now.year
    month = now.month

    all_users = User.objects.all()

    for user in all_users:
        send_account_summary_email(user, year, month)

