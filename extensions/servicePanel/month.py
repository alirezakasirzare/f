from services.models import ServicesOrders
import datetime

def month(user_id):
    date_now = str(datetime.datetime.now()).split(' ')[0].replace('-',',')
    date_spilt = date_now.split(',')
    date = datetime.date(int(date_spilt[0]),int(date_spilt[1]),int(date_spilt[2]))
    orders = []
    for i in range(30):
        days = datetime.timedelta(i)
        date_week = str(date - days).split('-')
        products = ServicesOrders.objects.filter(service__service_user_id=user_id,date__year=date_week[0], date__month=date_week[1],date__day=date_week[2],payment_status=True).order_by('id').all()
        orders.append(sum([p.price for p in products]))
    return orders

