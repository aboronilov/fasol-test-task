from rest_framework import viewsets
from .serializers import SenderSerializer
from .models import Sender


class SenderViewSet(viewsets.ModelViewSet):
    serializer_class = SenderSerializer
    queryset = Sender.objects.all()

