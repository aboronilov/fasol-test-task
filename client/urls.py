from django.urls import path, include
from rest_framework import routers

from .views import ClientViewSet

router = routers.DefaultRouter()
router.register('client', ClientViewSet, basename="client")

app_name = "client"
urlpatterns = [
    path("", include(router.urls))
]
