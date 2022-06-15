from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.carts_page, name='carts_page'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]