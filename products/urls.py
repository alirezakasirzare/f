from django.urls import path
from . import views

app_name = 'products'

urlpatterns =[
       path('', views.products_list_page,name='products_list_page'),
       path('detail/<int:id>/<str:slug>/', views.product_detail_page,name='product_detail_page'),
       path('tracking/', views.product_tracking_page,name='products_tracking_page'),
]

