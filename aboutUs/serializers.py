from rest_framework import serializers
from .models import AboutUs

class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'