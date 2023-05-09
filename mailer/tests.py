from django.urls import reverse
from rest_framework.test import APITestCase
from client.models import Client
from mailer.models import Mailer
from message.models import Message
from django.utils import timezone

class MailerTest(APITestCase):
    def setUp(self):
        self.url = reverse("mailer:mailer-list")
        self.phones = ["79001234567", "79001234568", "79111234568"]
        self.contents = ["Message for all clients"]  
    
    def get_clients(self):
        for item in self.phones:
            Client.objects.create(phone=item)        
    
    def get_mailers(self):
        for item in self.contents:
            Mailer.objects.create(
                content=item,
                start=timezone.now()-timezone.timedelta(minutes=5),
                finish=timezone.now()+timezone.timedelta(hours=5)
            )  

    def test_messaged_created_after_mailers_creation(self):
        for item in self.phones:
            Client.objects.create(phone=item) 
      
        for item in self.contents:
            Mailer.objects.create(
                content=item,
                start=timezone.now()-timezone.timedelta(minutes=5),
                finish=timezone.now()+timezone.timedelta(hours=5)
            )    
        messages = Message.objects.all().count()
        assert messages == len(self.phones)