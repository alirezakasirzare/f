from django.contrib import admin
from .models import Userperson

@admin.register(Userperson)
class personadmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'image', 'phone_auth']
