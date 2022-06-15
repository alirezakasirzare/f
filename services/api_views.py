from rest_framework.permissions import IsService,IsAuthenticated
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from extensions.services import best
from rest_framework import status
from django.db.models import Q
from .serializers import *
from .models import *


class services_list(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        return Services.objects.all().order_by('id')

class services_detail(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return [get_object_or_404(Services,id=id)]

class services_search(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        q = self.request.query_params.get('q',False)
        return Services.objects.filter(title__icontains=q).all().order_by('id')



class services_filter(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        hour = self.request.query_params.get('hour',False)
        gender = self.request.query_params.get('gender',False)
        categories = self.request.query_params.get('categories',False)
        company = self.request.query_params.get('company',False)
        return Services.objects.filter(Q(categories__name=categories,service_user__gender=gender,company__icontains=company,service_reservation__hour__icontains=hour)).distinct().order_by('id')



class services_best(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):

        return Services.objects.filter(id__in=best()).order_by('-id')



class services_sliders(generics.ListAPIView):
    queryset = ServicesSliders.objects.all().order_by('id')
    serializer_class = ServicesSlidersSerizalizers


class services_similar(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        service = get_object_or_404(Services,id=id)
        return Services.objects.filter(categories__id__in=[s.id for s in service.categories.all()]).order_by('-id')



class services_comments_list(generics.ListAPIView):
    serializer_class = ServicesCommentsSerizalizers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return ServicesComments.objects.filter(service_id=id,status=True).all()



class services_comments_add(generics.CreateAPIView):
    serializer_class = ServicesCommentsSerizalizers

    def post(self, request, *args, **kwargs):
        data = ServicesCommentsSerizalizers(data=request.data)
        if data.is_valid():
            vl = data.validated_data
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            service_comment_check = ServicesComments.objects.filter(user_id=token_info.user.id,service_id=vl['service'].id,status=False).first()
            if service_comment_check is None:
                ServicesComments.objects.create(user_id=token_info.user.id,service_id=vl['service'].id,comment=vl['comment'],status=False)
                return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': 'شما قبلا دیدگاه ثبت کرده اید'})
        else:
            return Response(data.errors)


class services_scores_number(generics.ListAPIView):
    serializer_class = ServicesScoresSerizalizers

    def get(self, request, format=None):
        id = self.request.query_params.get('id',False)
        info = ServicesScores.objects.filter(service_id=id).all()
        scores = [score.score for score in info]
        return Response({'number': sum(scores)})


class services_scores_search(generics.ListAPIView):
    serializer_class = ServicesScoresSerizalizers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        id = self.request.query_params.get('id',False)
        info = get_object_or_404(ServicesScores,user_id=token_info.user.id,service_id=id)
        return Response({"number": info.score})


class services_scores_add(generics.CreateAPIView):
    serializer_class = ServicesScoresSerizalizers

    def post(self, request, *args, **kwargs):
        data = ServicesScoresSerizalizers(data=request.data)
        if data.is_valid():
            vl = data.validated_data
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            scores_check = ServicesScores.objects.filter(user_id=token_info.user.id,service_id=vl['service'].id).first()
            if scores_check is None:
                ServicesScores.objects.create(user_id=token_info.user.id,service_id=vl['service'].id,score=vl['score'])
                return Response({'message': 'با موفقیت ثبت  شد'})
            else:
                return Response({'message': 'شما قبلا امتیاز ثبت کرده اید'})
        else:
            return Response(data.errors)


class services_complaints_add(generics.CreateAPIView):
    serializer_class = ServicesComplaintsSerializers
    permission_classes = [IsService]

    def post(self,request):
        data = ServicesComplaintsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            order = ServicesOrders.objects.filter(service_id=data.validated_data['service'],user_id=token_info.user.id,payment_status=True).first()
            if order is not None:
                ServicesComplaints_check = ServicesComplaints.objects.filter(service__service_user_id=token_info.user.id,service_id=data.validated_data['service']).first()
                if ServicesComplaints_check is None:
                    ServicesComplaints(user_id=token_info.user.id, service_id=data.validated_data['service'],text=data.validated_data['text']).save()
                    return Response({'message': 'شکایت ثبت شد'})
                else:
                    return Response({"message": "کاربر قبلا برای این محصول شکایت ثبت کرده است"})
            else:
                return Response({'message': 'شما این محصول رو خریداری نکردید'})
        else:
            return Response(data.errors)



class services_categories_list(generics.ListAPIView):
    serializer_class = ServicesCategoriesSerializers
    queryset = ServicesCategories.objects.order_by('id').all()


class services_filter_category(generics.ListAPIView):
    serializer_class = ServicesSerizalizers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return get_list_or_404(Services,categories__id__in=[id])