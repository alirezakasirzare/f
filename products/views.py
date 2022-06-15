from django.shortcuts import get_object_or_404,redirect, render
from rest_framework.authtoken.models import Token
from siteSettings.models import SiteSettings
from .models import *

"""
Views :

    product_list() # View all products per page
    product_detail() # View details of every product
    
"""



def products_list_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "محصولات"

    context = {
        'title': title,
    }
    return render(request, 'Products/products_list_page/products_list_page.html', context)


def product_detail_page(request, id,slug):
    product = get_object_or_404(Products, pk=id, slug=slug)
    seller_info = Sellers.objects.filter(id=product.seller.id).first()
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + f"{product.title}"
    token = Token.objects.filter(user_id=request.user.id).first()


    context = {
        'title': title,
        'product': product,
        'seller_info': seller_info,
        'token': token,

    }

    return render(request, 'Products/product_detail_page/product_detail_page.html', context)


def product_tracking_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + f"پیگیری محصول"

    context = {
        'title': title,
    }

    return render(request,'Products/products_tracking_page/products_tracking_page.html',context)
