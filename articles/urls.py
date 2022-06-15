from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.articles_list_page,name='articles_list_page'),
    path('<str:label>/',views.articles_list_filter_labels_page,name='articles_list_filter_labels_page'),
    path('detail/<int:id>/<str:slug>/',views.article_detail_page,name='article_detail_page'),
]
