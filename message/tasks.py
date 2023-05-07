from celery import shared_task

@shared_task
def send_message(data, client_id, sender_id):
    pass