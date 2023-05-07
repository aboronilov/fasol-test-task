from django.db import models
from sender.models import Sender
from client.models import Client
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q
from .tasks import send_message


class Message(models.Model):
    created_at = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    is_send = models.BooleanField(verbose_name='Sending status', default=False)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Message with id {self.id} for client with id {self.client.id} and status {self.is_send}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

@receiver(post_save, sender=Sender)    
def sender_created_handler(sender, instance, created, *args, **kwargs):
    lookup = (
        Q(operator_code=instance.operpator_code) |
        Q(tag=instance.tag) | 
        Q(tag__in=instance.tag())
    )
    clients = Client.object.filter(lookup)
    for client in clients:
        # если рассылка только создана - значит сообщения создаются впервые
        if created:
            message = Message.objects.create(
                sender=instance,
                client=client
            )
            message.save()

            data = {
                "id": message.id,
                "phone": client.phone,
                "text": instance.content
            }
            send_message(data=data, client_id=client.id, sender_id=instance.id)
        # если редактируется, значит сообщения тоже нужно редактировать
        else:
            messages = Message.objects.filter(
                sender=instance,
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
