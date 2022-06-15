from services.models import ServicesMessages,ServicesUsersMessages
from sellers.models import SellersMessages,SellersUsersMessages
from products.models import ProductsScores,ProductsComments
from customizedUserModel.models import Userperson
from django.db.models.fields import TextField
from services.models import ServicesOrders
from rest_framework import serializers
from carts.models import Orders

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



class OrdersSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Orders
        fields = '__all__'


class ServicesOrdersSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = ServicesOrders
        fields = '__all__'

class ProdcutsScoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsScores
        fields = '__all__'

class ProdcutsCommentsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    product_image = serializers.ReadOnlyField()
    product_title = serializers.ReadOnlyField()
    class Meta:
        model = ProductsComments
        fields = '__all__'

class SellersMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SellersMessages
        fields = '__all__'
        extra_kwargs = {
            "seller": {"error_messages": {"required": "This amount is required"}},
            "user": {"read_only": True}
        }

    def validate(self, attrs):
        if attrs.get('file'):
            file = str(attrs.get('file')).split('.')[::-1][0]
            if file in ['html','php','js','py','css']:
                raise serializers.ValidationError({f'{file}': "پسوند  فایل مجاز نیست!"})
            else:
                return attrs
        else:
            return attrs


class SellersUsersMessagesSerializers(serializers.ModelSerializer):
    seller_fullname = serializers.ReadOnlyField()
    seller_image = serializers.ReadOnlyField()
    class Meta:
        model = SellersUsersMessages
        fields = '__all__'



class ServiceMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesMessages
        fields = '__all__'
        extra_kwargs = {
            "service": {"error_messages": {"required": "This amount is required"}},
            "user": {"read_only": True}
        }

    def validate(self, attrs):
        if attrs.get('service'):
            if attrs.get('file'):
                file = str(attrs.get('file')).split('.')[::-1][0]
                if file in ['html','php','js','py','css']:
                    raise serializers.ValidationError({f'{file}': "پسوند  فایل مجاز نیست!"})
                else:
                    return attrs
            else:
                return attrs
        else:
            raise serializers.ValidationError({f'service': "این مقدار الزامی است!"})


class ServiceUsersMessagesSerializers(serializers.ModelSerializer):
    service_fullname = serializers.ReadOnlyField()
    service_image = serializers.ReadOnlyField()
    class Meta:
        model = ServicesUsersMessages
        fields = '__all__'
