from django.urls import path
from . import views

app_name = 'aboutUs'

urlpatterns = [
    path('',views.aboutus_page,name='aboutus_page'),
]
