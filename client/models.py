from django.db import models
from django.core.validators import RegexValidator
import pytz

TIMEZONE_CHOICES = zip(pytz.all_timezones, pytz.all_timezones)
phone_regex = RegexValidator(regex=r'^7\d{10}$',
                             message="Please provide your mobile phone in the format 7XXXXXXXXXX")


class Client(models.Model):
    phone = models.CharField(verbose_name='Phone number', 
                             validators=[phone_regex], 
                             unique=True, 
                             max_length=11)
    tag = models.CharField(verbose_name='Search tags', 
                           max_length=100, 
                           blank=True)
    timezone = models.CharField(verbose_name='Time zone', 
                                max_length=32, 
                                choices=TIMEZONE_CHOICES, 
                                default='UTC')    
  
    def __str__(self):
        return f'Client with id - {self.id} and number - {self.phone}'
        
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'