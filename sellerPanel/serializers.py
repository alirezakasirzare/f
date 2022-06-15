from customizedUserModel.models import Userperson
from django.db.models.fields import TextField
from rest_framework import serializers
from carts.models import Orders
from sellers.models import *
from products.models import *

class SellersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = '__all__'
        extra_kwargs = {
            'business_owner': {'write_only': True}
        }



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


class ProductsSerializers(serializers.ModelSerializer):
    dimensions = serializers.CharField(required=True)
    weight = serializers.CharField(required=True)
    class Meta:
        model = Products
        fields = '__all__'




class ProductsUpdateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    dimensions = serializers.CharField(required=False)
    weight = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    main_image = serializers.ImageField(required=False)
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    image3 = serializers.ImageField(required=False)
    image4 = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)
    short_description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    discounted_price = serializers.IntegerField(required=False)
    seller = serializers.CharField(required=False)
    maincategories = serializers.PrimaryKeyRelatedField(queryset=ProductMainCategories.objects.all(), many=True,required=False)
    subCategories1 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_1.objects.all(), many=True,required=False)
    subCategories2 = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategories_2.objects.all(), many=True,required=False)
    colors = serializers.PrimaryKeyRelatedField(queryset=ProductsColors.objects.all(), many=True,required=False)
    sizes = serializers.PrimaryKeyRelatedField(queryset=ProductsSizes.objects.all(), many=True,required=False)
    score = serializers.IntegerField(required=False)
    inventory = serializers.IntegerField(required=False)
    class Meta:
        model = Products
        fields = '__all__'


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.dimensions = validated_data.get('dimensions', instance.dimensions)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.main_image = validated_data.get('main_image', instance.main_image)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.image2 = validated_data.get('image2', instance.image2)
        instance.image3 = validated_data.get('image3', instance.image3)
        instance.image4 = validated_data.get('image4', instance.image4)
        instance.description = validated_data.get('description', instance.description)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.price = validated_data.get('price', instance.price)
        instance.discounted_price = validated_data.get('discounted_price', instance.discounted_price)
        instance.maincategories.set(validated_data.get('maincategories', instance.maincategories))
        instance.subCategories1.set(validated_data.get('subCategories1', instance.subCategories1))
        instance.subCategories2.set(validated_data.get('subCategories2', instance.subCategories2))
        instance.colors.set(validated_data.get('colors', instance.colors))
        instance.sizes.set(validated_data.get('sizes', instance.sizes))
        instance.score = validated_data.get('score', instance.score)
        instance.inventory = validated_data.get('inventory', instance.inventory)
        instance.save()
        return instance




class ProductsCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComments
        fields = '__all__'





class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'





class ProductsComplaintsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsComplaints
        fields = '__all__'




class SellersMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SellersMessages
        fields = '__all__'
        extra_kwargs = {
            "user": {"error_messages": {"required": "This amount is required"}},
        }

    def validate(self, attrs):
        if attrs.get('user') is None:
            raise serializers.ValidationError({f'user': "این  مقدار الزامی است !"})

        elif attrs.get('file'):
            file = str(attrs.get('file')).split('.')[::-1][0]
            if file in ['html', 'php', 'js', 'py', 'css']:
                raise serializers.ValidationError({f'{file}': "پسوند  فایل مجاز نیست!"})
            else:
                return attrs
        else:
            return attrs





class SellersUsersMessagesSerializers(serializers.ModelSerializer):
    user_fullname = serializers.ReadOnlyField()
    user_image = serializers.ReadOnlyField()
    class Meta:
        model = SellersUsersMessages
        fields = '__all__'










