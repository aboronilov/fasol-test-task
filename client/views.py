from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

