from django.contrib import admin
from .models import *

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['writer','title','date']

@admin.register(ArticlesHits)
class ArticlesHitsAdmin(admin.ModelAdmin):
    list_display = ['ip','article']

@admin.register(ArticlesLabels)
class ArticlesLabelsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ArticlesLikes)
class ArticlesLikesAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(ArticlesComments)
class ArticlesCommentsAdmin(admin.ModelAdmin):
    list_display = ['comment']
