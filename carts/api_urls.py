from django.urls import path
from . import api_views

app_name = 'ApiCarts'

urlpatterns = [
    path('carts-list/',api_views.carts_list.as_view(),name='carts_list'),
    path('carts-number/',api_views.carts_number.as_view(),name='carts_number'),
    path('carts-add/',api_views.carts_add.as_view(),name='carts_add'),
    path('carts-remove/',api_views.carts_remove.as_view(),name='carts_remove'),
]