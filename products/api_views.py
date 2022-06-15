from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework import generics
from extensions.products import *
from django.db.models import Q
from carts.models import *
from .serializers import *
from .models import *
from random import choices
from string import ascii_letters


class products_list(generics.ListAPIView):
    queryset = Products.objects.filter(status=True,inventory__gt=0).all().order_by('id')
    serializer_class = ProdcutsSerializers


class products_detail(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        slug = self.request.query_params.get('slug',False)
        return [get_object_or_404(Products,id=id,slug=slug,status=True,inventory__gt=0)]


class products_similar(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        product = Products.objects.filter(id=id,status=True,inventory__gt=0).first()
        return get_list_or_404(Products,maincategories__id__in=[ mainC.id for mainC in product.maincategories.all()],status=True,inventory__gt=0)



class product_next(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = int(self.request.query_params.get('id',False))
        return [get_object_or_404(Products,id=id+1,status=True,inventory__gt=0)]


class product_previous(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        id = int(self.request.query_params.get('id',False))
        return [get_object_or_404(Products,id=id-1,status=True,inventory__gt=0)]



class products_search(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        q = self.request.query_params.get('q',False)
        return Products.objects.filter(title__icontains=q,status=True,inventory__gt=0).all().order_by('id')


class products_sliders(generics.ListAPIView):
    queryset = ProductsSliders.objects.all().order_by('id')
    serializer_class = ProductsSlidersSerializers




class products_filter(generics.ListAPIView):
    serializer_class = ProdcutsSerializers


    def get_queryset(self):
        price1 = self.request.query_params.get('price1',False)
        price2 = self.request.query_params.get('price2',False)
        categories = self.request.query_params.get('categories',False)
        colors = self.request.query_params.get('colors',False)
        sller_type = self.request.query_params.get('sller_type',False)
        return Products.objects.filter(Q(maincategories__name=categories,status=True,inventory__gt=0) | Q(colors__products=colors,status=True) | Q(price=price1,status=True) | Q(price=price2,status=True) | Q(discounted_price=price1,status=True) | Q(discounted_price=price2,status=True) | Q(seller__business_categories=sller_type,status=True)).distinct().order_by('id')

class products_filter_main_category_info(generics.ListAPIView):
    serializer_class = ProdcutsMainCategoriesSerializers


    def get_queryset(self):
        category_id = self.request.query_params.get('id',False)
        return [get_object_or_404(ProductMainCategories,id=category_id,status=True)]


class products_filter_category(generics.ListAPIView):
    serializer_class = ProdcutsSerializers


    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return get_list_or_404(Products,maincategories__id__in=[id],status=True)

class products_filter_sub_category2(generics.ListAPIView):
    serializer_class = ProdcutsSerializers


    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return get_list_or_404(Products,maincategories__products__subCategories2__id__in=[id],status=True)


class products_main_categories(generics.ListAPIView):
    queryset = ProductMainCategories.objects.filter(status=True).all()
    serializer_class = ProdcutsMainCategoriesSerializers

class products_sub_categories1(generics.ListAPIView):
    serializer_class = ProdcutsMainCategoriesSerializers

    def get(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('id', False)
        result = [{s1.id:s1.name} for s1 in ProductSubCategories_1.objects.filter(productmaincategories__id=category_id).all()]
        return Response(result)

class products_sub_categories2(generics.ListAPIView):
    serializer_class = ProdcutsMainCategoriesSerializers

    def get(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('id', False)
        result = [{s2.id:s2.name} for s2 in ProductSubCategories_2.objects.filter(productsubcategories_1__id=category_id).all()]
        return Response(result)


class products_colors(generics.ListAPIView):
    queryset = ProductsColors.objects.all()
    serializer_class = ProductsColorsSerializers





class products_sellers_typs(generics.ListAPIView):
    queryset = SellersCategories.objects.all()
    serializer_class = ProductsSellersCategoriesSerializers




class products_comments_list(generics.ListAPIView):
    serializer_class = ProductsCommentsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return ProductsComments.objects.filter(product_id=id,status=True).order_by('id').all()





class products_discounts(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=latest_discounts_products(),status=True).order_by('id')



class products_offers(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=specialProducts(),status=True,inventory__gt=0).order_by('id')


class products_mostexpensive(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=most_expensive_prodcuts(),status=True,inventory__gt=0).order_by('id')





class products_cheapest(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=cheapest_products(),status=True,inventory__gt=0).order_by('id')



class products_bestselling(generics.ListAPIView):
    serializer_class = ProdcutsSerializers

    def get_queryset(self):
        return Products.objects.filter(id__in=BestSelling_products(),status=True,inventory__gt=0).order_by('id')





class products_newest(generics.ListAPIView):
    queryset = Products.objects.filter(status=True,inventory__gt=0).all().order_by('-id')
    serializer_class = ProdcutsSerializers


class products_score_number(generics.ListAPIView):
    serializer_class = ProductsScoresSerializers

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        info = ProductsScores.objects.filter(product_id=id).all()
        scores = [score.score for score in info]
        return Response({'number': sum(scores)})

class products_score_search(generics.ListAPIView):
    serializer_class = ProductsScoresSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        info = get_object_or_404(ProductsScores,product_id=id,user_id=token_info.user.id)
        return Response({'number': info.score})


class products_score_add(generics.CreateAPIView):
    serializer_class = ProductsScoresSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsScoresSerializers(data=request.data)
        if data.is_valid():
            if data.validated_data['score'] <=5 and  not(data.validated_data['score'] < 1) :
                user_token = str(request.headers['Authorization']).split('Token')[1].strip()
                token_info = Token.objects.filter(key=user_token).first()
                ProductsScores_check = ProductsScores.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id).first()
                if ProductsScores_check is None:
                    ProductsScores(user_id=token_info.user.id, product_id=data.validated_data['product'].id,score=data.validated_data['score']).save()
                    return Response({'message': 'امتیاز ثبت شد'})
                else:
                    return Response({"message": "کاربر قبلا برای این محصول امتیاز ثبت کرده است"})
            else:
                return Response({'message': 'حداکثر امتیاز 5 است'})
        else:
            return Response(data.errors)







class products_comments_add(generics.CreateAPIView):
    queryset = ProductsComments
    serializer_class = ProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = ProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                ProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه ثبت شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)




class products_complaints_add(generics.CreateAPIView):
    serializer_class = ProductsComplaintsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsComplaintsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            order = Orders.objects.filter(product_id=data.validated_data['product'],cart__user_id=token_info.user.id,payment_status=True).first()
            if order is not None:
                ProductsComplaints_check = ProductsComplaints.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product']).first()
                if ProductsComplaints_check is None:
                    ProductsComplaints(user_id=token_info.user.id, product_id=data.validated_data['product'],text=data.validated_data['text']).save()
                    return Response({'message': 'شکایت ثبت شد'})
                else:
                    return Response({"message": "کاربر قبلا برای این محصول شکایت ثبت کرده است"})
            else:
                return Response({'message': 'شما این محصول رو خریداری نکردید'})
        else:
            return Response(data.errors)



class products_tracking_code_status(generics.ListAPIView):
    serializer_class = ProductsTrackingCodeSerializers

    def get_queryset(self):
        code = self.request.query_params.get('code',False)
        return [get_object_or_404(ProductsTrackingCode,tracking_code=code)]


class products_tracking_code_add(generics.CreateAPIView):
    serializer_class = ProductsTrackingCodeSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = ProductsTrackingCodeSerializers(data=request.data)
        if data.is_valid():
            cart = Carts.objects.filter(id=data.validated_data['cart'].id,user_id=request.user.id,payment_status=True).first()
            tracking_code_check = ProductsTrackingCode.objects.filter(cart_id=cart.id).first()
            if tracking_code_check is not None:
                return Response({'tracking_code': tracking_code_check.tracking_code})
            else:
                def create():
                    tracking_code = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
                    tracking_code_check = ProductsTrackingCode.objects.filter(tracking_code=tracking_code).first()
                    if tracking_code_check is not None:
                        create()
                    else:
                        return tracking_code

                tracking_code_create = ProductsTrackingCode.objects.create(cart_id=data.validated_data['cart'].id,tracking_code=create(),code_status=False,product_status='confirming')
                return Response({'tracking_code': tracking_code_create.tracking_code})
        else:
            return Response(data.errors)


class products_tracking_code_edit(generics.UpdateAPIView):
    serializer_class = ProductsTrackingCodeSerializers
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        data = ProductsTrackingCodeSerializers(data=request.data)
        if data.is_valid():
            cart = Carts.objects.filter(id=data.validated_data['cart'].id,user_id=request.user.id,payment_status=True).first()
            tracking_code_check = ProductsTrackingCode.objects.filter(cart_id=cart.id).first()
            if tracking_code_check.code_status != True and tracking_code_check.product_status != 'processed':
                data.update(tracking_code_check, data.validated_data)
                return Response({'message': ' بروزرسانی شد'})
            else:
                return Response({'message': 'محصول تحویل داده شده'})
        else:
            return Response(data.errors)