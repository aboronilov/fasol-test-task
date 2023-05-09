from rest_framework import viewsets
from .serializers import MessageSerizlier
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from django.core.mail import send_mail
from django.conf import settings


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerizlier
    queryset = Message.objects.all()

    @action(detail=False, methods=['get'])
    def stat(self, request):
        total_count = self.queryset.count()
        sent = self.queryset.filter(is_send=True)
        not_sent = self.queryset.filter(is_send=False)
        not_sent_ids = []
        for item in not_sent:
            not_sent_ids.append(item.pk)
        
        if not_sent.count() > 0:
            message = f"Total counter - {total_count} sent - {sent.count()}. Not sent - {not_sent.count()} with ids {not_sent_ids}"
        else:
            message = f"Total counter - {total_count}. All of the messages are sent succesfully"

        send_mail(
            subject="Message stat",
            message=message,
            from_email=settings.EMAIL_HOST_PASSWORD,
            recipient_list=[settings.EMAIL_RECIEVER],
            fail_silently=False,                        
        )
        
        return Response({"message": message})
        

