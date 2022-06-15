from django.contrib import admin
from .models import *

@admin.register(ServicesCategories)
class SServicesCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ServicesCompanies)
class ServicesCompaniesAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_user','date']
    search_fields = ['service_user']


@admin.register(ServicesCollaborationHours)
class ServicesCollaborationHoursAdmin(admin.ModelAdmin):
    list_display = ['service_user','hour']
    search_fields = ['service_user']



@admin.register(ServicesSliders)
class ServicesSlidersAdmin(admin.ModelAdmin):
    list_display = ['image']
    


@admin.register(ServicesComments)
class ServicesCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    search_fields = ['user','comment']

@admin.register(ServicesScores)
class ServicesScoresAdmin(admin.ModelAdmin):
    list_display = ['score']


@admin.register(ServicesOrders)
class ServicesOrdersAdmin(admin.ModelAdmin):
    list_display = ['price']


@admin.register(ServicesComplaints)
class ServicesComplaintsAdmin(admin.ModelAdmin):
    list_display = ['text']

@admin.register(ServicesUsersMessages)
class ServicesUsersMessagesAdmin(admin.ModelAdmin):
    list_display = ['user','service']

@admin.register(ServicesMessages)
class ServicesMessagesAdmin(admin.ModelAdmin):
    list_display = ['text','user','service']