from .models import Message
from mailer.models import Mailer
from client.models import Client
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q
from message.tasks import send_message
from django.utils import timezone

@receiver(post_save, sender=Mailer, dispatch_uid="handle_mailer_create")    
def handle_mailer_create(sender, instance, created, *args, **kwargs):
    current_time = timezone.now()
    clients = Client.objects.all()
    if instance.tag is not None or instance.operator_code is not None:
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

            # в зависимости от времени начала рассылки применяем сразу же или делаем отсрочку
            if instance.start <= current_time <= instance.finish:
                send_message.delay(message.pk, client.phone, instance.content)
            else:
                send_message.apply_async((message.pk, client.phone, instance.content), eta=instance.start)
        # если редактируется, значит существующие сообщения тоже нужно редактировать
        else:
            messages = Message.objects.filter(
                mailer=instance,
                client=client
            )
            for message in messages:
                message.mailer = instance
                message.cilent = client
                message.is_send = False
                message.save()

                # в зависимости от времени начала рассылки применяем сразу же или делаем отсрочку
                if instance.start <= current_time <= instance.finish:
                    send_message.delay(message.pk, client.phone, instance.content)
                else:
                    send_message.apply_async(message.pk, client.phone, instance.content, eta=instance.start)