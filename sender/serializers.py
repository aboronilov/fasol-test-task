from rest_framework import serializers
from .models import Sender
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class SenderSerializer(serializers.ModelSerializer):
    to_send = serializers.SerializerMethodField()

    class Meta:
        model = Sender
        fields = [
            "id",
            "content",
            "start",
            "finish",
            "tag",
            "operpator_code"
        ]

    def validate(self, attrs):
        current_time = now()
        if current_time > attrs["finish"]:
            raise ValidationError("Sending date is later the current date")
        
        if attrs["start"] >= attrs["finish"]:
            raise ValidationError("Sending start date is later or equal than the end")
        
        if len(attrs["operpator_code"]) != 3:
            raise ValidationError("Operpator code should consist of 3 symbols")
        
        return super().validate(attrs)


