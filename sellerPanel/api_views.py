from rest_framework.authtoken.models import Token
from customizedUserModel.models import Userperson
from rest_framework.permissions import IsSeller
from extensions.sellerPanel.month import month
from rest_framework.response import Response
from extensions.sellerPanel.year import year
from extensions.sellerPanel.week import week
from extensions.sellerPanel.day import day
from rest_framework import generics
from sellers.models import Sellers
from rest_framework import status
from .serializers import *




class sellerpanel_shop_add(generics.CreateAPIView):
    serializer_class = SellersSerializers
    permission_classes = [IsSeller]

    def post(self, request, *args, **kwargs):
        data = SellersSerializers(data=request.data)
        if data.is_valid():
            seller = Sellers.objects.filter(business_owner_id=request.user.id).first()
            if seller is None:
                data.save()
                data.instance.business_owner_id = request.user.id
                data.save()
                user = Userperson.objects.filter(id=request.user.id).first()
                user.is_active = False
                user.save()
                return Response({'message': 'اطلاعات فروشگاه شما ثبت شد منتظر تایید باشید'})
            else:
                return Response({'message': 'شما قبلا اطلاعات فروشگاه خود را اضافه کرده اید'})
        else:
            return Response(data.errors)

class sellerpanel_edit_account(generics.UpdateAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsSeller]

    def update(self, request, *args, **kwargs):
        data = UsersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Userperson.objects.filter(id=token_info.user.id).first()
            data.update(user, data.validated_data)
            return Response({'message': 'با موفقیت بروز شد'})
        else:
            return Response(data.errors)


class sellerpanel_user_info(generics.ListAPIView):
    permission_classes = [IsSeller]


    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Userperson.objects.filter(id=token_info.user.id).first()
        if user is not None:
            result = {
                'id': user.id,
                'fullname': user.fullname,
                'phone': user.phone,
                'image': user.image.url,
            }
            return Response({'result': result})
        else:
            return Response({'message': 'empty'})


class sellerpanel_products_add(generics.CreateAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsSeller]

    def post(self, request, *args, **kwargs):
        data = ProductsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            seller = Sellers.objects.filter(business_owner_id=token_info.user.id).first()
            if seller is not None:
                data.save()
                data.instance.seller = seller
                data.save()
                return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': 'خطا با پشتیبانی تماس بگیرید'},status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(data.errors)


class sellerpanel_products_edit(generics.UpdateAPIView):
    serializer_class = ProductsUpdateSerializers
    permission_classes = [IsSeller]

    def post(self, request, *args, **kwargs):
        data = ProductsUpdateSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            seller = Sellers.objects.filter(business_owner_id=token_info.user.id).first()
            if seller is not None:
                product = Products.objects.filter(id=data.validated_data['id'],seller_id=seller.id).first()
                data.update(product,data.validated_data)
                return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': 'خطا با پشتیبانی تماس بگیرید'},status=status.HTTP_408_REQUEST_TIMEOUT)

        else:
            return Response(data.errors)


class sellerpanel_products_delete(generics.ListAPIView):
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        product = Products.objects.filter(id=id,seller__business_owner_id=token_info.user.id).first()
        if product is not None:
            product.delete()
            return Response({'message': 'با موفقیت حذف شد'})
        else:
            return Response({'message': 'محصولی پیدا نشد'},status=status.HTTP_400_BAD_REQUEST)


class sellerpanel_products_list(generics.ListAPIView):
    serializer_class = ProductsSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Products.objects.filter(status=True,seller__business_owner_id=token_info.user.id).all().order_by('id')


class sellerpanel_products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsComments.objects.filter(product__seller__business_owner_id=token_info.user.id).all().order_by('id')

class sellerpanel_products_orders_list(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Orders.objects.filter(product__seller__business_owner_id=token_info.user.id,payment_status=True).all().order_by('id')


class sellerpanel_products_complaints_list(generics.ListAPIView):
    serializer_class = ProductsComplaintsSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsComplaints.objects.filter(product__seller__business_owner_id=token_info.user.id).all().order_by('id')

class sellerpanel_products_complaints_user_info(generics.ListAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Userperson.objects.filter(id=id).first()
        orders = Orders.objects.filter(cart__user_id=user.id).first()
        if user is not None and orders is not None:
            return Response({'phone': user.phone})
        else:
            return Response({'message': 'کاربر پیدا نشد'})

class sellerpanel_products_sales_chart_day(generics.ListAPIView):
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = day(token_info.user.id)
        return Response({'total_price': total_price})

class sellerpanel_products_sales_chart_week(generics.ListAPIView):
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = week(token_info.user.id)
        return Response({'total_price': total_price})

class sellerpanel_products_sales_chart_month(generics.ListAPIView):
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = month(token_info.user.id)
        return Response({'total_price': total_price})

class sellerpanel_products_sales_chart_year(generics.ListAPIView):
    permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = year(token_info.user.id)
        return Response({'total_price': total_price})

class sellerpanel_messages_add(generics.CreateAPIView):
    serializer_class = SellersMessagesSerializers
    permission_classes = [IsSeller]

    def post(self, request, *args, **kwargs):
        data = SellersMessagesSerializers(data=request.data)
        if data.is_valid():
            seller = Sellers.objects.filter(business_owner_id=request.user.id).first()
            if seller is not None:
                usermessages = SellersUsersMessages.objects.filter(user_id=data.validated_data['user'],seller_id=seller.id).first()
                if usermessages is None:
                    SellersUsersMessages.objects.create(user_id=data.validated_data['user'].id,seller_id=seller.id)
                else:
                    pass
                data.save()
                data.instance.seller_id = seller.id
                data.save()
                id = str(data.instance)
                message = SellersMessages.objects.filter(id=id).first()
                message.is_seller = True
                message.save()
                return Response({'message': 'با موفقیت ثبت شد'})
            else:
                return Response({'message': 'خطا با پشتیبانی تماس بگیرید'},status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(data.errors)



class sellerpanel_messages_list_filter(generics.ListAPIView):
    serializer_class = SellersMessagesSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        user_id = self.request.query_params.get('id',False)
        return SellersMessages.objects.filter(seller__business_owner_id=self.request.user.id,user_id=user_id).order_by('-id').all()


class sellerpanel_users_messages_list(generics.ListAPIView):
    serializer_class = SellersUsersMessagesSerializers
    permission_classes = [IsSeller]

    def get_queryset(self):
        return SellersUsersMessages.objects.filter(seller__business_owner_id=self.request.user.id).order_by('-id').all()


