from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from products.models import Products
from rest_framework import generics
from .models import Carts,Orders
from .serializers import *


class carts_list(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        cart = Carts.objects.filter(user_id=token_info.user.id).first()
        orders = Orders.objects.filter(cart_id=cart.id,payment_status=False).all()
        return orders



class carts_number(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        cart = Carts.objects.filter(user_id=token_info.user.id).first()
        orders = Orders.objects.filter(cart_id=cart.id,payment_status=False).count()
        return Response({'number': orders})


class carts_add(generics.CreateAPIView):
    serializer_class = OrdersSerializers

    def post(self, request, *args, **kwargs):
        user_token = str(request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        carts_check = Carts.objects.filter(user_id=token_info.user.id,payment_status=False).first()
        if carts_check is None:
            carts_create = Carts.objects.create(user_id=token_info.user.id,payment_status=False)
        else: pass

        data = OrdersSerializers(data=request.data)
        if data.is_valid():
            vl = data.validated_data
            cart = Carts.objects.filter(user_id=token_info.user.id).first()
            product = Products.objects.filter(id=vl['product'].id,status=True).first()
            price = product.discounted_price if product.discounted_price != 0 else product.price
            order = Orders.objects.create(product_id=product.id,title=product.title,description=product.description,price=price,seller_id=product.seller.id,cart_id=cart.id,size_id=vl['size'],color_id=vl['color'])
            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)

class carts_remove(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        order_id = request.GET.get('orderid', False)
        product_id = request.GET.get('productid', False)
        cart = Carts.objects.filter(user_id=request.user.id,payment_status=False).first()
        order = Orders.objects.filter(id=order_id, product_id=product_id, cart_id=cart.id,payment_status=False).first()
        if order is not None:
            order.delete()
            return Response({'message': 'با موفقیت حذف شد'})
        else:
            return Response({'order': 'وجود ندارد '})
