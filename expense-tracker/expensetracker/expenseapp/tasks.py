# tasks.py
from celery import shared_task
from datetime import datetime
from .utils import send_account_summary_email

@shared_task
def send_account_summary_emails():
    now = datetime.now()
    year = now.year
    month = now.month
    # Replace this with a query to get all users
    users = YourUserModel.objects.all()

    for user in users:
        send_account_summary_email(user, year, month)
