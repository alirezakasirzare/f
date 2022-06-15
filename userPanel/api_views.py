from sellers.models import SellersMessages,SellersUsersMessages,Sellers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from customizedUserModel.models import Userperson
from rest_framework.response import Response
from rest_framework import generics
from services.models import Services
from .serializers import *


class userpanel_edit_account(generics.UpdateAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]


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

class userpanel_user_info(generics.ListAPIView):
    permission_classes = [IsAuthenticated]


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


class userpanel_order_history(generics.ListAPIView):
    serializer_class = OrdersSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Orders.objects.filter(cart__user_id=token_info.user.id,payment_status=True).all().order_by('id')




class userpanel_services_received(generics.ListAPIView):
    serializer_class = ServicesOrdersSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ServicesOrders.objects.filter(user_id=token_info.user.id,payment_status=True).all().order_by('id')




class userpanel_products_scores_list(generics.ListAPIView):
    serializer_class = ProdcutsScoresSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsScores.objects.filter(user_id=token_info.user.id).all().order_by('id')



class userpanel_products_scores_list(generics.ListAPIView):
    serializer_class = ProdcutsScoresSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsScores.objects.filter(user_id=token_info.user.id).all().order_by('id')




class userpanel_products_comments_list(generics.ListAPIView):
    serializer_class = ProdcutsCommentsSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ProductsComments.objects.filter(user_id=token_info.user.id).all().order_by('id')




class userpanel_seller_messages_add(generics.CreateAPIView):
    serializer_class = SellersMessagesSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = SellersMessagesSerializers(data=request.data)
        if data.is_valid():
            seller = Sellers.objects.filter(business_owner_id=data.validated_data['seller'].id).first()
            usermessages = SellersUsersMessages.objects.filter(user_id=request.user.id,seller_id=seller.id).first()
            if usermessages is None:
                SellersUsersMessages.objects.create(user_id=request.user.id, seller_id=seller.id)
            else:
                pass
            data.save()
            data.instance.user_id = request.user.id
            data.save()
            return Response({'message': 'با موفقیت ثبت شد'})
        else:
            return Response(data.errors)




class userpanel_seller_messages_list_filter(generics.ListAPIView):
    serializer_class = SellersMessagesSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        seller_id = self.request.query_params.get('id',False)
        return SellersMessages.objects.filter(user_id=self.request.user.id,seller_id=seller_id).order_by('-id').all()


class userpanel_seller_users_messages_list(generics.ListAPIView):
    serializer_class = SellersUsersMessagesSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return SellersUsersMessages.objects.filter(user_id=self.request.user.id).order_by('-id').all()





class userpanel_service_messages_add(generics.CreateAPIView):
    serializer_class = ServiceMessagesSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = ServiceMessagesSerializers(data=request.data)
        if data.is_valid():
            service = Services.objects.filter(id=data.validated_data['service'].id).first()
            usermessages = ServicesUsersMessages.objects.filter(user_id=request.user.id,service_id=service.id).first()
            if usermessages is None:
                ServicesUsersMessages.objects.create(user_id=request.user.id, service_id=service.id)
            else:
                pass
            data.save()
            data.instance.user_id = request.user.id
            data.save()
            return Response({'message': 'با موفقیت ثبت شد'})
        else:
            return Response(data.errors)




class userpanel_service_messages_list_filter(generics.ListAPIView):
    serializer_class = ServiceMessagesSerializers
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        service_id = self.request.query_params.get('id',False)
        return ServicesMessages.objects.filter(user_id=self.request.user.id,service=service_id).order_by('-id').all()


class userpanel_service_users_messages_list(generics.ListAPIView):
    serializer_class = ServiceUsersMessagesSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ServicesUsersMessages.objects.filter(user_id=self.request.user.id).order_by('-id').all()


