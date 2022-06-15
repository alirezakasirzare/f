from django.contrib.auth import authenticate,login,logout
from siteSettings.models import SiteSettings,Codes
from customizedUserModel.models import Userperson
from rest_framework.authtoken.models import Token
from django.shortcuts import render,redirect
from .fomrs import RegisterForm
from extensions.sms import send_sms
from django.contrib import messages
from random import randint

def login_page(request):
    if not request.user.is_authenticated:

        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "ورود کاربران"
        context = {
            'title': title,
        }
        if request.method == "POST":
            phone = str(request.POST['phone'])
            if phone.isdigit() and len(phone) == 11:
                user = Userperson.objects.filter(phone=phone).first()
                if user is not None:
                    code_check = Codes.objects.filter(user=user,status=False).count()
                    if code_check == 6:
                        return redirect('contactUs:contactus_page')
                    else:
                        code = randint(10000,50000)
                        save_code = Codes.objects.create(user=user,code=code).save()
                        send_sms(phone,f' کد تایید شما : {code}')
                        return redirect('accounts:code_authentication_page',phone=phone)
                else:
                    messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                    return render(request, 'Accounts/login_page/login_page.html',context)
            else:
                messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                return render(request, 'Accounts/login_page/login_page.html',context)



        return render(request,'Accounts/login_page/login_page.html',context)

    else:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.role == "user":
            return redirect('userPanel:userpanel_page')

        elif user.role == 'seller':
            return redirect('sellerPanel:sellerpanel_page')

        elif user.role == 'service':
            return redirect('servicePanel:servicepanel_page')

        elif user.is_superuser:
            return redirect('admin_panel')
        else:
            return redirect('/')



def code_authentication_page(request,phone):
    if not request.user.is_authenticated:

        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "احراز هویت کاربر"
        context = {
            'title': title,
        }

        if request.method == "POST":
            code = request.POST['code']
            user = Userperson.objects.filter(phone=phone).first()
            code_check = Codes.objects.filter(code=code,user=user,status=False).first()
            if code_check is not None:
                if user is not None:
                    codes = Codes.objects.filter(code=code,user=user,status=False).all()
                    for code in codes: codes.delete()

                    if user.status == False:
                        user.status = True
                        user.save()

                    token = Token.objects.filter(user_id=user.id).first()
                    if token is None:
                        Token.objects.create(user_id=user.id)

                    login(request, user)

                    if user.role == "user":
                        return redirect('userPanel:userpanel_page')

                    elif user.role == 'seller':
                        return redirect('sellerPanel:sellerpanel_page')

                    elif user.role == 'service':
                        return redirect('servicePanel:servicepanel_page')

                    elif user.is_superuser:
                        return redirect('admin_panel')
                else:
                    return redirect('/')

            else:
                messages.error(request,'کد  تایید اشتباه است')
                return render(request,'Accounts/code_authentication_page/code_authentication_page.html',context)

        return render(request,'Accounts/code_authentication_page/code_authentication_page.html',context)

    else:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.role == "user":
            return redirect('userPanel:userpanel_page')

        elif user.role == 'seller':
            return redirect('sellerPanel:sellerpanel_page')

        elif user.role == 'service':
            return redirect('servicePanel:servicepanel_page')

        elif user.is_superuser:
            return redirect('admin_panel')
        else:
            return redirect('/')



def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('Accounts:login_page')
    else:
        return redirect('Accounts:login_page')



def register_page(request,type):
    if not request.user.is_authenticated:
        if type in ['seller','user','service']:
            site_settings = SiteSettings.objects.last()
            title = site_settings.site_name + " - " + "ثبت نام "
            form = RegisterForm(request.POST , request.FILES or None)
            context = {
                'title': title,
                'form': form,
            }

            if request.method == "POST":
                if form.is_valid():
                    cl = form.cleaned_data
                    create_user = Userperson.objects.create(phone=cl['phone'],fullname=cl['fullname'],image=cl['image'],address=cl['address'],gender=cl['gender'])
                    create_user.role = type
                    create_user.set_password(cl['password'])
                    create_user.save()
                    login(request,create_user)

                    token = Token.objects.filter(user_id=create_user.id).first()
                    if token is None:
                        Token.objects.create(user_id=create_user.id)

                    if create_user.role == "user":
                        return redirect('userPanel:userpanel_page')

                    elif create_user.role == 'seller':
                        return redirect('sellerPanel:sellerpanel_page')

                    elif create_user.role == 'service':
                        return redirect('servicePanel:servicepanel_page')

                    elif create_user.is_superuser:
                        return redirect('admin_panel')
                    else:
                        return redirect('/')

                else:
                    messages.error(request,form.errors)
                    return render(request, 'Accounts/register_page/register_page.html', context)
            else:
                context['form'] = RegisterForm(None)
                return render(request, 'Accounts/register_page/register_page.html', context)



        else:
            return redirect('Accounts:login_page')
    else:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user.role == "user":
            return redirect('userPanel:userpanel_page')

        elif user.role == 'seller':
            return redirect('sellerPanel:sellerpanel_page')

        elif user.role == 'service':
            return redirect('servicePanel:servicepanel_page')

        elif user.is_superuser:
            return redirect('admin_panel')
        else:
            return redirect('/')
