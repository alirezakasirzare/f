from django.urls import path
from . import api_views

app_name = 'ApiSiteSettings'

urlpatterns = [
    path('settings/',api_views.site_settings.as_view(),name='site_settings'),
    path('social-networks/',api_views.social_networks.as_view(),name='social_networks'),
]