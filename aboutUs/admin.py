from django.contrib import admin
from .models import AboutUs

@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ('description','team_image')
