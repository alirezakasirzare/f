from customizedUserModel.models import Userperson
from django.db.models.fields import TextField
from rest_framework import serializers
from services.models import *


class UsersSerializers(serializers.ModelSerializer):
    fullname = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    address = TextField(null=True,blank=True)
    phone_auth = serializers.BooleanField(required=False)
    password = serializers.CharField(required=False)
    class Meta:
        model = Userperson
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.image = validated_data.get('image', instance.image)
        if instance.password != validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        else: pass

        instance.save()
        return instance

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServicesUpdateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    company = serializers.CharField(source='company.id',required=False)
    image = serializers.ImageField(required=False)
    description = TextField(blank=True,null=True)
    short_description = TextField(blank=True,null=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=ServicesCategories.objects.all(), many=True,required=False)


    class Meta:
        model = Services
        fields = '__all__'
        extra_kwargs = {"short_description": {"required": False, "allow_null": True},"description": {"required": False, "allow_null": True}}

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.company = validated_data.get('company', instance.company)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.categories.set(validated_data.get('categories',instance.categories))
        instance.save()
        return instance


class ServicesComplaintsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesComplaints
        fields = '__all__'



class ServicesCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesComments
        fields = '__all__'



class ServicesOrdersSerializers(serializers.ModelSerializer):
    user_fullname = serializers.ReadOnlyField()
    class Meta:
        model = ServicesOrders
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('user') is None:
            raise serializers.ValidationError({f'user': "این  مقدار الزامی است !"})
        else:
            return attrs


class ServicesMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesMessages
        fields = '__all__'
        extra_kwargs = {
            "user": {"error_messages": {"required": "This amount is required"}},
            "service": {"error_messages": {"required": "This amount is required"}},
        }

    def validate(self, attrs):
        if attrs.get('user') is None:
            raise serializers.ValidationError({f'user': "این  مقدار الزامی است !"})

        elif attrs.get('service') is None:
            raise serializers.ValidationError({f'service': "این  مقدار الزامی است !"})


        elif attrs.get('file'):
            file = str(attrs.get('file')).split('.')[::-1][0]
            if file in ['html', 'php', 'js', 'py', 'css']:
                raise serializers.ValidationError({f'{file}': "پسوند  فایل مجاز نیست!"})
            else:
                return attrs
        else:
            return attrs



class ServicesUsersMessagesSerializers(serializers.ModelSerializer):
    user_fullname = serializers.ReadOnlyField()
    user_image = serializers.ReadOnlyField()
    class Meta:
        model = ServicesUsersMessages
        fields = '__all__'



