from rest_framework import serializers
from .models import *

class ServicesSerizalizers(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    service_reservations = serializers.ReadOnlyField()
    service_user_fullname = serializers.ReadOnlyField()
    service_user_gender = serializers.ReadOnlyField()
    company_info = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Services
        fields = ['id','title','service_user_fullname','image','short_description','categories','jdate','service_reservations','service_user_fullname','service_user_gender','company_info']


class ServicesSlidersSerizalizers(serializers.ModelSerializer):
    class Meta:
        model = ServicesSliders
        fields = '__all__'

class ServicesCommentsSerizalizers(serializers.ModelSerializer):
    user_image = serializers.ReadOnlyField()
    user_fullname = serializers.ReadOnlyField()
    scores = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = ServicesComments
        fields = ['id','comment','user_fullname','user_image','scores','jdate','service']

    def validate(self, attrs):
        if attrs.get('service'):
            return attrs
        else:
            raise serializers.ValidationError({'service': 'این مقدار الزامی است'})


class ServicesScoresSerizalizers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = ServicesScores
        fields = '__all__'


class ServicesComplaintsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    service = serializers.IntegerField(required=True)
    class Meta:
        model = ServicesComplaints
        fields = '__all__'


class ServicesCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesCategories
        fields = '__all__'

