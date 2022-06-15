from django.contrib import admin
from .models import *

@admin.register(SiteSettings)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_number', 'email']
    search_filter = ['site_name', 'contact_number']

@admin.register(SocialNetworks)
class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ['instagram', 'whatsapp', 'youtube']


@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    list_display = ['code']

