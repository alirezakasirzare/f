from rest_framework import serializers
from .models import Orders


class OrdersSerializers(serializers.ModelSerializer):
    size = serializers.CharField(required=True)
    color = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Orders
        fields = '__all__'
        extra_kwargs = {
            "product": {"error_messages": {"required": "This amount is required"}},
        }

