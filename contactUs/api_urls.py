from django.urls import path
from . import api_views


app_name = 'ApiContactUs'

urlpatterns = [
    path('contactus-list/',api_views.contactus_list.as_view(),name='contactus_list'),
    path('add-contact/',api_views.add_contact.as_view(),name='add_contact'),
]