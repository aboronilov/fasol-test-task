from django.db import models
from mailer.models import Mailer
from client.models import Client


class Message(models.Model):
    created_at = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    is_send = models.BooleanField(verbose_name='Sending status', default=False)
    mailer = models.ForeignKey(Mailer, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Message with id {self.id} for client with id {self.client.id} and status {self.is_send}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


