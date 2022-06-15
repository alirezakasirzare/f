from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.response import Response
from extensions.articles import topArticles
from .models import Articles,ArticlesLikes
from rest_framework import generics
from rest_framework import status
from .serializers import *




class articles_list(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.all().order_by('id')



class articles_detail(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        slug = self.request.query_params.get('slug',False)
        return [get_object_or_404(Articles,id=id,slug=slug)]


class articles_search(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        q = self.request.query_params.get('q',False)
        return Articles.objects.filter(title__icontains=q).all().order_by('id')



class articles_filter_labels(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        q = self.request.query_params.get('q',False)
        return Articles.objects.filter(labels__name__icontains=q).all().order_by('id')




class articles_latest(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.all().order_by('-id')[:5]


class articles_top(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.filter(id__in=topArticles())




class articles_comment_add(generics.CreateAPIView):
    serializer_class = ArticlesCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = ArticlesCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            article_comment_check = ArticlesComments.objects.filter(user_id=token_info.user.id,article_id=data.validated_data['article'].id,status=False).first()
            if article_comment_check is None:
                ArticlesComments.objects.create(article_id=data.validated_data['article'].id,user_id=token_info.user.id,comment=data.validated_data['comment'],status=False)
                return Response({"message": "دیدگاه ثبت شد"})
            else:
                return Response({"message": "کاربر از قبل دیدگاه ثبت کرده است"},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(data.errors)


class articles_comment_list(generics.ListAPIView):
    serializer_class = ArticlesCommentsSerializers


    def get_queryset(self):
        id = self.request.query_params.get('id')
        return ArticlesComments.objects.filter(article_id=id,status=True).all()


class articles_comment_number(generics.ListAPIView):
    serializer_class = ArticlesCommentsSerializers
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        id = self.request.query_params.get('id',False)
        comments = ArticlesComments.objects.filter(article_id=id).count()
        return Response({'number': comments})




class articles_like_add(generics.CreateAPIView):
    serializer_class = ArticlesLikesializers
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = ArticlesLikesializers(data=request.data)
        if data.is_valid():
            article_id = data.validated_data['article'].id
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            check_like = ArticlesLikes.objects.filter(user_id=token_info.user.id, article_id=article_id).first()
            if check_like is None:
                add_like = ArticlesLikes.objects.create(user_id=token_info.user.id, article_id=article_id)
                return Response({"message": "اضافه شد"})
            else:
                return Response({"message": "از قبل اضافه شده بود"})
        else:
            return Response(data.errors)
        
        
class articles_like_number(generics.ListAPIView):
    serializer_class = ArticlesLikesializers
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        id = self.request.query_params.get('id',False)
        likes = ArticlesLikes.objects.filter(article_id=id).count()
        return Response({'number': likes})


        
class articles_hits_add(generics.CreateAPIView):
    serializer_class = ArticlesHitsSializers
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = ArticlesHitsSializers(data=request.data)
        if data.is_valid():
            check_hits = ArticlesHits.objects.filter(article=data.validated_data['article'], ip=data.validated_data['ip']).first()
            if check_hits is None:
                add_hits = ArticlesHits.objects.create(article=data.validated_data['article'], ip=data.validated_data['ip'])
                return Response({"message": "اضافه شد"})
            else:
                return Response({"message": "از قبل اضافه شده بود"})
        else:
            return Response(data.errors)



class articles_hits_number(generics.ListAPIView):
    serializer_class = ArticlesHitsSializers
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        id = self.request.query_params.get('id',False)
        hits = ArticlesHits.objects.filter(article_id=id).count()
        return Response({'number': hits})


