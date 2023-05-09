from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ClientTest(APITestCase):
    def setUp(self):
        self.url = reverse('client:client-list')

    def test_user_created_with_correct_data(self):        
        data = {
            'phone': '79001234567',
            'timezone': 'Europe/Moscow',
        }
        request = self.client.post(self.url, data, format='json')
        
        assert request.status_code == status.HTTP_201_CREATED
   
    def test_user_is_not_created_with_wrong_phone(self):
        data = {
            'phone': '7',
        }
        request = self.client.post(self.url, data, format='json')

        assert request.status_code == 400

    def test_user_is_not_created_with_wrong_timezone(self):
        data = {
            'phone': '79001234567',
            'timezone': 'wrong_timezone',
        }
        request = self.client.post(self.url, data, format='json')

        assert request.status_code == status.HTTP_400_BAD_REQUEST  
    

