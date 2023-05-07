from django.urls import path, include
from rest_framework import routers

from .views import MessageViewSet

router = routers.SimpleRouter()
router.register('message', MessageViewSet, basename="message")

app_name = "message"
urlpatterns = [
    path("", include(router.urls))
]