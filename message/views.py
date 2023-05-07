from rest_framework import viewsets
from .serializers import MessageSerizlier
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerizlier
    queryset = Message.objects.all()


