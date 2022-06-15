from django.urls import path
from . import views

app_name = 'userPanel'

urlpatterns = [
    path('',views.userpanel_page,name='userpanel_page'),
    path('chatlist',views.userpanel_chatlist_page,name='userpanel_chatlist_page'),
    path('chat-seller',views.userpanel_chat_seller_page,name='userpanel_chat_seller_page'),
    path('chat-service',views.userpanel_chat_service_page,name='userpanel_chat_service_page'),
]