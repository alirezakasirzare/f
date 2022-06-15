from .serializers import AboutUsSerializers
from rest_framework import generics
from .models import AboutUs


class about_us(generics.ListAPIView):
    serializer_class = AboutUsSerializers

    def get_queryset(self):
        return AboutUs.objects.first()