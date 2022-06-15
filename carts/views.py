from rest_framework.authtoken.models import Token
from products.models import ProductsTrackingCode
from siteSettings.models import SiteSettings
from config.settings import ALLOWED_HOSTS
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from extensions.sms import send_sms
from string import ascii_letters
from random import choices
from carts.models import *
import datetime
import requests
import json

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
CallbackURL = f'/carts/verify/' #ALLOWED_HOSTS[0]




def send_request(request):
    orders = Orders.objects.filter(payment_status=False,cart__user_id=request.user.id).all()
    if len(orders) > 0:
        global amount
        amount = f'{sum([order.price for order in orders])}0'
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
        return redirect('/')



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
                orders = Orders.objects.filter(payment_status=False, cart__user_id=request.user.id).all()
                cart = Carts.objects.filter(user_id=request.user.id, payment_status=False).first()
                for order in orders:
                    order.payment_status = True
                    order.payment_date = datetime.datetime.now()
                    order.save()
                    product = Products.objects.filter(id=order.product.id).first()
                    product.inventory -= order.count
                    product.save()

                cart.payment_status = True
                cart.payment_date = datetime.datetime.now()
                cart.save()

                def create():
                    tracking_code = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
                    tracking_code_check = ProductsTrackingCode.objects.filter(tracking_code=tracking_code).first()
                    if tracking_code_check is not None:
                        create()
                    else:
                        return tracking_code

                code = create()
                tracking_code_create = ProductsTrackingCode.objects.create(cart_id=cart.id, tracking_code=code,code_status=False,product_status='confirming')
                send_sms(cart.user.phone, f''' محصول خریداری شد\n\nکد پیگیری : {code}''')
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


def carts_page(request):
    if request.user.is_authenticated:
        site_settings = SiteSettings.objects.last()
        user = Userperson.objects.filter(id=request.user.id).first()
        title = site_settings.site_name + " - " + "سد خرید"
        token = Token.objects.filter(user_id=request.user.id).first()

        context = {
            'title': title,
            'address': user.address,
            'token': token,

        }

        return render(request,'Carts/carts_page/carts_page.html',context)
    else:
        return redirect('accounts:login_page')