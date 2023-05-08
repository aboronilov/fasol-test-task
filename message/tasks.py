from notification.celery import app
from .models import Message
from time import sleep
from django.conf import settings
import requests 
from requests import exceptions
import json


@app.task
def send_message(message_id, client_id, text):
    headers = {
        'Authorization': f'Bearer {settings.SENDER_TOKEN}',
        'Content-Type': 'application/json'
    }
    url = f"{settings.MESSAGE_SENDER_URL}{message_id}"
    data = {
        "id": message_id,
        "phone": client_id,
        "text": text
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        # logger
        for _ in range(5):
            try:
                response = requests.post(url=url, headers=headers, data=json.dumps(data) ,timeout=10)
            except exceptions.ConnectionError:
                sleep(15)
            except exceptions.Timeout:
                sleep(30)
            else:
                # logger
                break
    
    message = Message.objects.get(pk=data["id"])
    message.is_send = True
    message.save()
