from notification.celery import app
from .models import Message
from django.conf import settings
import requests 
import json


@app.task(name="send.message", bind=True, max_retries=10)
def send_message(self, message_id, client_id, text):
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

    try:
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
    except Exception:
        # logger
        self.retry(coundtdown=5, **self.request.retries)
    else:
        message = Message.objects.get(pk=data["id"])
        message.is_send = True
        message.save()
        # logger
    
    return('sender', response.status_code)
