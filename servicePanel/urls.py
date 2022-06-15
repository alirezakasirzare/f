from django.urls import path
from . import views

app_name = "servicePanel"

urlpatterns = [
    path('',views.servicepanel_page,name='servicepanel_page'),
    path('chatlist',views.servicepanel_chatlist_page,name='servicepanel_chatlist_page'),
    path('chat',views.servicepanel_chat_page,name='servicepanel_chat_page'),
]