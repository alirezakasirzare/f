from carts.models import Orders
import datetime

def year(user_id):
    date_now = str(datetime.datetime.now()).split(' ')[0].replace('-',',')
    date_spilt = date_now.split(',')
    date = datetime.date(int(date_spilt[0]),int(date_spilt[1]),int(date_spilt[2]))
    orders = []
    for i in range(365):
        days = datetime.timedelta(i)
        date_week = str(date - days).split('-')
        products = Orders.objects.filter(seller__business_owner_id=user_id,payment_date__year=date_week[0], payment_date__month=date_week[1],payment_date__day=date_week[2],payment_status=True).order_by('id').all()
        orders.append(sum([p.price for p in products]))

    return orders