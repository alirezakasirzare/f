from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('code-authentication/<str:phone>/',views.code_authentication_page,name='code_authentication_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('register/<str:type>/',views.register_page,name='register_page'),
]