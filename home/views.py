from siteSettings.models import SiteSettings
from extensions.products import *
from django.shortcuts import render
from articles.models import Articles
from products.models import Products

def home_page(request):
    latest_articles = Articles.objects.all().order_by('-id')[:3]
    special_products = Products.objects.filter(id__in=specialProducts())
    best_selling_products = Products.objects.filter(id__in=BestSelling_products())
    LatestDiscountsProducts = Products.objects.filter(id__in=latest_discounts_products())
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "صفحه اصلی"




    context = {
        'latest_articles': latest_articles,
        'prodcuts_extensions': special_products,
        'best_selling_products': best_selling_products,
        'LatestDiscountsProducts': LatestDiscountsProducts,
        'title': title,
    }
    return render(request,'Home/home_page/home_page.html',context)
