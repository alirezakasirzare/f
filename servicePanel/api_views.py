from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsService
from extensions.servicePanel.month import month
from rest_framework.response import Response
from extensions.servicePanel.year import year
from extensions.servicePanel.week import week
from extensions.servicePanel.day import day
from rest_framework import generics,status
from rest_framework.reverse import reverse
from services.models import *
from .serializers import *


class servicepanel_edit_account(generics.UpdateAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsService]

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


class servicepanel_user_info(generics.ListAPIView):
    permission_classes = [IsService]


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

class servicepanel_service_add(generics.CreateAPIView):
    serializer_class = ServicesSerializers
    permission_classes = [IsService]

    def post(self, request, *args, **kwargs):
        data = ServicesSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.service_user_id = token_info.user.id
            data.save()
            return Response({'message': 'با موفقیت اضافه شد شد'})
        else:
            return Response(data.errors)

class servicepanel_service_edit(generics.UpdateAPIView):
    serializer_class = ServicesUpdateSerializers
    permission_classes = [IsService]

    def update(self, request, *args, **kwargs):
        data = ServicesUpdateSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            service = Services.objects.filter(id=data.validated_data['id'],service_user_id=token_info.user.id).first()
            data.update(service, data.validated_data)
            return Response({'message': 'با موفقیت بروز شد'})
        else:
            return Response(data.errors)


class servicepanel_service_delete(generics.ListAPIView):
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        service = Services.objects.filter(id=id,service_user_id=token_info.user.id).first()
        if service is not None:
            service.delete()
            return Response({'message': 'با موفقیت حذف شد'})
        else:
            return Response({'message': 'سرویسی وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)


class servicepanel_service_list(generics.ListAPIView):
    serializer_class = ServicesSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return Services.objects.filter(service_user_id=token_info.user.id).all()


class servicepanel_service_complaints_list(generics.ListAPIView):
    serializer_class = ServicesComplaintsSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return ServicesComplaints.objects.filter(service__service_user_id=token_info.user.id).all().order_by('id')

class servicepanel_service_complaints_user_info(generics.ListAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Userperson.objects.filter(id=id).first()
        orders = ServicesOrders.objects.filter(user_id=user.id).first()
        if user is not None and orders is not None:
            return Response({'phone': user.phone})
        else:
            return Response({'message': 'کاربر پیدا نشد'})



class servicepanel_service_comments_list(generics.ListAPIView):
    serializer_class = ServicesCommentsSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        services = Services.objects.filter(service_user_id=token_info.user.id).all().order_by('id')
        comments = ServicesComments.objects.filter(service_id__in=[s.id for s in services]).order_by('id')
        return comments


class servicepanel_service_orders_list(generics.ListAPIView):
    serializer_class = ServicesOrdersSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Userperson.objects.filter(id=id).first()
        services = Services.objects.filter(service_user_id=token_info.user.id).all().order_by('id')
        orders = ServicesOrders.objects.filter(service_id__in=[s.id for s in services],payment_status=True).order_by('id')
        return orders


class servicepanel_service_sales_chart_day(generics.ListAPIView):
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = day(token_info.user.id)
        return Response({'total_price': total_price})

class servicepanel_service_sales_chart_week(generics.ListAPIView):
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = week(token_info.user.id)
        return Response({'total_price': total_price})

class servicepanel_service_sales_chart_month(generics.ListAPIView):
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = month(token_info.user.id)
        return Response({'total_price': total_price})

class servicepanel_service_sales_chart_year(generics.ListAPIView):
    permission_classes = [IsService]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        total_price = year(token_info.user.id)
        return Response({'total_price': total_price})


class servicepanel_messages_add(generics.CreateAPIView):
    serializer_class = ServicesMessagesSerializers
    permission_classes = [IsService]

    def post(self, request, *args, **kwargs):
        data = ServicesMessagesSerializers(data=request.data)
        if data.is_valid():
            service = Services.objects.filter(id=data.validated_data['service'].id).first()
            usermessages = ServicesUsersMessages.objects.filter(user_id=data.validated_data['user'],service_id=service.id).first()
            if usermessages is None:
                ServicesUsersMessages.objects.create(user_id=data.validated_data['user'].id,service_id=service.id)
            else:
                pass
            data.save()
            data.instance.service_id = service.id
            data.save()
            id = str(data.instance)
            message = ServicesMessages.objects.filter(id=id).first()
            message.is_service = True
            message.save()
            return Response({'message': 'با موفقیت ثبت شد'})
        else:
            return Response(data.errors)



class servicepanel_messages_list_filter(generics.ListAPIView):
    serializer_class = ServicesMessagesSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        user_id = self.request.query_params.get('id',False)
        return ServicesMessages.objects.filter(service__service_user_id=self.request.user.id,user_id=user_id).order_by('-id').all()


class servicepanel_users_messages_list(generics.ListAPIView):
    serializer_class = ServicesUsersMessagesSerializers
    permission_classes = [IsService]

    def get_queryset(self):
        return ServicesUsersMessages.objects.filter(service__service_user_id=self.request.user.id).order_by('-id').all()



class servicepanel_create_link_payment(generics.CreateAPIView):
    serializer_class = ServicesOrdersSerializers
    permission_classes = [IsService]

    def post(self, request, *args, **kwargs):
        data = ServicesOrdersSerializers(data=request.data)
        if data.is_valid():
            vl = data.validated_data
            service_order = ServicesOrders.objects.create(user_id=vl['user'].id,service_id=vl['service'].id,price=vl['price'])
            return Response({'link': reverse('services:request', args=[service_order.id])})
        else:
            return Response(data.errors)

