# myapp/tasks.py
from celery import shared_task # This looks inside the installed celery library
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
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


@shared_task
def notify_user_task():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications", # The group name
        {
            "type": "send_notification",
            "message": "Background Task Finished!"
        }
    )