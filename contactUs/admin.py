from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactModelAdmiin(admin.ModelAdmin):
    list_display = ('firstName','lastName','contact_number','company_name','subject','message')
    search_filter = ('firstName','lastName', 'contact_number', 'subject')

