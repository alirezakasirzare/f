from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from customizedUserModel.models import Userperson
from siteSettings.models import SiteSettings,Codes
from django.shortcuts import render,redirect
from extensions.sms import send_sms
from random import randint



def userpanel_page(request):
    if request.user.is_authenticated:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.status == True:
            token = Token.objects.filter(user_id=request.user.id).first()
            site_settings = SiteSettings.objects.last()
            title = site_settings.site_name + " - " + "پنل کاربری"
            context = {
                'title': title,
                'token': token,
            }
            return render(request,'UserPanel/userpanel_page/userpanel_page.html',context)
        else:
            code_check = Codes.objects.filter(user_id=user.id, status=False).count()
            if code_check == 6:
                return redirect('contactUs:contactus_page')
            else:
                code = randint(10000, 50000)
                save_code = Codes.objects.create(user=user, code=code).save()
                send_sms(user.phone, f' کد تایید شما : {code}')
                logout(request)
                return redirect('accounts:code_authentication_page', phone=user.phone)

    else:
        return redirect('accounts:login_page')



def userpanel_chat_seller_page(request):
    if request.user.is_authenticated:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.status == True:
            site_settings = SiteSettings.objects.last()
            token = Token.objects.filter(user_id=request.user.id).first()
            title = site_settings.site_name + " - " + "پنل کاربری"
            context = {
                'title': title,
                'token': token,
            }
            return render(request,'UserPanel/userpanel_page/userpanel_chat_seller_page.html',context)
        else:
            code_check = Codes.objects.filter(user_id=user.id, status=False).count()
            if code_check == 6:
                return redirect('ContactUs:contactus_page')
            else:
                code = randint(10000, 50000)
                save_code = Codes.objects.create(user=user, code=code).save()
                send_sms(user.phone, f' کد تایید شما : {code}')
                logout(request)
                return redirect('Accounts:code_authentication_page', phone=user.phone)

    else:
        return redirect('Accounts:login_page')

def userpanel_chat_service_page(request):
    if request.user.is_authenticated:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.status == True:
            token = Token.objects.filter(user_id=request.user.id).first()
            site_settings = SiteSettings.objects.last()
            title = site_settings.site_name + " - " + "پنل کاربری"
            context = {
                'title': title,
                'token': token,
            }
            return render(request,'UserPanel/userpanel_page/userpanel_chat_service_page.html',context)
        else:
            code_check = Codes.objects.filter(user_id=user.id, status=False).count()
            if code_check == 6:
                return redirect('ContactUs:contactus_page')
            else:
                code = randint(10000, 50000)
                save_code = Codes.objects.create(user=user, code=code).save()
                send_sms(user.phone, f' کد تایید شما : {code}')
                logout(request)
                return redirect('Accounts:code_authentication_page', phone=user.phone)

    else:
        return redirect('Accounts:login_page')


def userpanel_chatlist_page(request):
    if request.user.is_authenticated:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.status == True:
            site_settings = SiteSettings.objects.last()
            token = Token.objects.filter(user_id=request.user.id).first()
            title = site_settings.site_name + " - " + "پنل کاربری"
            context = {
                'title': title,
                'token': token,
            }
            return render(request,'UserPanel/userpanel_page/userpanel_chatlist_page.html',context)
        else:
            code_check = Codes.objects.filter(user_id=user.id, status=False).count()
            if code_check == 6:
                return redirect('ContactUs:contactus_page')
            else:
                code = randint(10000, 50000)
                save_code = Codes.objects.create(user=user, code=code).save()
                send_sms(user.phone, f' کد تایید شما : {code}')
                logout(request)
                return redirect('Accounts:code_authentication_page', phone=user.phone)

    else:
        return redirect('Accounts:login_page')
