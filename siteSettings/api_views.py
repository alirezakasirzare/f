from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from .serializers import *
from .models import *



class site_settings(generics.ListAPIView):
    serializer_class = SiteSettingsSerializers
    queryset = SiteSettings.objects.order_by('id').all()[:1]
    permission_classes = [IsAdminUser]



class social_networks(generics.ListAPIView):
    serializer_class = SocialNetworksSerializers
    queryset = SocialNetworks.objects.order_by('id').all()[:1]

