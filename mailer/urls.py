from django.urls import path, include
from rest_framework import routers

from .views import MailerViewSet

router = routers.DefaultRouter()
router.register('mailer', MailerViewSet, basename="mailer")

app_name = "mailer"
urlpatterns = [
    path("", include(router.urls))
]