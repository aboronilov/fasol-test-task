from django.db import models
from sender.models import Sender
from client.models import Client
from client.serializers import ClientSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q
from .tasks import send_message


class Message(models.Model):
    created_at = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    is_send = models.BooleanField(verbose_name='Sending status', default=False)
    mailer = models.ForeignKey(Sender, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Message with id {self.id} for client with id {self.client.id} and status {self.is_send}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

@receiver(post_save, sender=Sender)    
def sender_created_handler(sender, instance, created, *args, **kwargs):
    clients = Client.objects.all()
    if instance.tag or instance.operator_code is not None:
        lookup = (
            Q(tag=instance.tag) |
            Q(operator_code=instance.operator_code)
        )
        clients = Client.objects.filter(lookup)
    for client in clients:
        # если рассылка только создана - значит сообщения создаются впервые
        if created:
            message = Message.objects.create(
                mailer=instance,
                client=client
            )
            message.save()

            data = {
                "id": message.id,
                "phone": client.phone,
                "text": instance.content
            }
            send_message(data=data, client_id=client.id, sender_id=instance.id)
        # если редактируется, значит существующие сообщения тоже нужно редактировать
        else:
            messages = Message.objects.filter(
                mailer=instance,
                client=client
            )
            for message in messages:
                message.sender = sender
                message.cilent = client
                message.is_send = False
                message.save()

                data = {
                    "id": message.id,
                    "phone": client.phone,
                    "text": instance.content
                }
                send_message(data=data, client_id=client.id, sender_id=instance.id)
