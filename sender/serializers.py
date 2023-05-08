from rest_framework import serializers
from .models import Sender
from django.core.exceptions import ValidationError
from django.utils import timezone

class SenderSerializer(serializers.ModelSerializer):
    content = serializers.ReadOnlyField()
    start = serializers.ReadOnlyField()
    finish = serializers.ReadOnlyField()
    tag = serializers.ReadOnlyField()
    operator_code = serializers.ReadOnlyField()
    class Meta:
        model = Sender
        fields = [
            "id",
            "content",
            "start",
            "finish",
            "tag",
            "operator_code"
        ]

    def validate(self, attrs):
        if attrs["finish"] <= timezone.now():
            raise ValidationError("Sending date is later the current date")
        
        if attrs["start"] >= attrs["finish"]:
            raise ValidationError("Sending start date is later or equal than the end")
        
        if len(attrs["operator_code"]):
            if len(attrs["operator_code"]) != 3:
                raise ValidationError("Operpator code should consist of 3 symbols")
        
        return super().validate(attrs)


