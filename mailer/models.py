from django.db import models


class Mailer(models.Model):
    content = models.TextField(verbose_name='Message content') 
    start = models.DateTimeField(verbose_name='Sending starts at')
    finish = models.DateTimeField(verbose_name='Sending finishes at')
    tag = models.CharField(verbose_name='Filter tag', max_length=32, blank=True, null=True)
    operator_code = models.CharField(verbose_name='Operator code filter', blank=True, null=True, max_length=3)

    def __str__(self):
        return f'Sending with id - {self.id} and content - {self.content}'
    
    class Meta:
        verbose_name = 'Mailer'
        verbose_name_plural = 'Mailers'