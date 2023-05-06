from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    operator_code = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            "id",
            "phone",
            "operator_code",
            "tag",
            "timezone"
        ]

    def get_operator_code(self, obj):
        return obj.phone[1:4]

    