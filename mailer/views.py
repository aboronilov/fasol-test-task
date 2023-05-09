from rest_framework import viewsets
from .serializers import MailerSerializer
from .models import Mailer


class MailerViewSet(viewsets.ModelViewSet):
    serializer_class = MailerSerializer
    queryset = Mailer.objects.all()

