from django.urls import path, include
from rest_framework import routers

from .views import SenderViewSet

router = routers.DefaultRouter()
router.register('sender', SenderViewSet, basename="sender")

app_name = "sender"
urlpatterns = [
    path("", include(router.urls))
]