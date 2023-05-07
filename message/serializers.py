from rest_framework import serializers
from .models import Message


class MessageSerizlier(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "id",
            "created_at",
            "is_send",
            "sender",
            "client"
        ]


