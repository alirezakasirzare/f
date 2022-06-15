from django.urls import path
from . import views

app_name = 'sellerPanel'

urlpatterns = [
    path('',views.sellerpanel_page,name='sellerpanel_page'),
    path('chatlist',views.sellerpanel_chatlist_page,name='sellerpanel_chatlist_page'),
    path('chat',views.sellerpanel_chat_page,name='sellerpanel_chat_page'),
]