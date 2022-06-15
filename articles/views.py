from .models import Articles,ArticlesHits,ArticlesLikes,ArticlesComments
from django.shortcuts import get_object_or_404,render,redirect
from extensions.articles import topArticles,visitor_ip_address
from rest_framework.authtoken.models import Token
from customizedUserModel.models import Userperson
from django.core.paginator import Paginator
from siteSettings.models import SiteSettings
from django.db.models import Q

"""

Views :

    articles_page() # View all articles And pagination
    article_page() # View an article
    
"""



def articles_list_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "مقالات"


    context = {
        'title': title,
    }
    return render(request,'Articles/articles_list_page/articles_list_page.html',context)

def articles_list_filter_labels_page(request,label):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "مقالات"


    context = {
        'title': title,
        'label': label,
    }
    return render(request,'Articles/articles_list_page/articles_list_page.html',context)




def article_detail_page(request,id,slug):
    article = get_object_or_404(Articles,pk=id,slug=slug)
    visitor_ip_address(request,article.id)
    article_hits = ArticlesHits.objects.filter(article_id=article.id).count()
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + f"{article.title}"
    like_count = ArticlesLikes.objects.filter(article_id=article.id).count()
    comment_count = ArticlesComments.objects.filter(article_id=article.id,status=True).count()
    comments = ArticlesComments.objects.filter(article_id=article.id,status=True).all()
    token = Token.objects.filter(user_id=request.user.id).first()


    context = {
        'title': title,
        'article': article,
        'comments': comments,
        'article_hits': article_hits,
        'like_count': like_count,
        'comment_count': comment_count,
        'token': token,
    }
    return render(request,'Articles/article_detail_page/article_detail_page.html',context)



