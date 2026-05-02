# myapp/tasks.py
from celery import shared_task # This looks inside the installed celery library
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Welcome to Our Site!',
        'Thank you for joining us!',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )
    
@shared_task
def check_celery_status():
    print("-----------------------------------------")
    print("SUCCESS: Celery is picking up tasks!")
    print("-----------------------------------------")
    return "Task Completed"