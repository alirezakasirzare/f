from rest_framework import serializers
from .models import *

class SiteSettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'

class SocialNetworksSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = ['instagram','whatsapp','youtube','telegram','facebook']
