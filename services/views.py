from rest_framework.authtoken.models import Token
from siteSettings.models import SiteSettings
from config.settings import ALLOWED_HOSTS
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from extensions.sms import send_sms
from services.models import *
import requests
import json

def services_list_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "خدمات"
    context = {
        'title': title,

    }

    return render(request,'Services/services_list_page/services_list_page.html',context)


def service_detail_page(request,id,slug):
    token = Token.objects.filter(user_id=request.user.id).first()
    context = {
        'token': token,

    }
    return render(request,'Services/service_detail_page/service_detail_page.html',context)


settings = SiteSettings.objects.first()
MERCHANT = f'{settings.payment_token}'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
#amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = f'{settings.email}'  # Optional
mobile = f'{settings.contact_number}'  # Optional
# Important: need to edit for realy server.
CallbackURL = f'/services/verify/' #ALLOWED_HOSTS[0]




def send_request(request,id):
    service_order_check = ServicesOrders.objects.filter(id=id).first()
    if service_order_check is not None:
        if service_order_check.payment_status != True:
            global order_id
            global amount
            order_id = id
            amount = f'{service_order_check.price}0'
            req_data = {
                "merchant_id": MERCHANT,
                "amount": amount,
                "callback_url": CallbackURL,
                "description": description,
                "metadata": {"mobile": mobile, "email": email}
            }
            req_header = {"accept": "application/json","content-type": "application/json'"}
            req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) == 0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return HttpResponse('قبلا پرداخت شده')
    else:
        return HttpResponse('404')


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                service_orders = ServicesOrders.objects.filter(id=order_id).first()
                service_orders.payment_status = True
                service_orders.save()
                send_sms(service_orders.service.service_user.phone,f'کاربر {service_orders.user.fullname} مبلغ {service_orders.price} تومن را پرداخت کرد ')
                return HttpResponse('Transaction success.\nRefID: ' + str(req.json()['data']['ref_id']))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(req.json()['data']['message']))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(req.json()['data']['message']))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')