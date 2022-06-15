from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('',views.services_list_page,name='services_list_page'),
    path('detail/<int:id>/<str:slug>/',views.service_detail_page,name='service_detail_page'),
    path('request/<int:id>/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]