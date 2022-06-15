from services.models import ServicesOrders
import datetime

def day(user_id):
    date_now = str(datetime.datetime.now()).split(' ')[0].replace('-',',')
    date_spilt = date_now.split(',')
    date = datetime.date(int(date_spilt[0]),int(date_spilt[1]),int(date_spilt[2]))
    # days = datetime.timedelta(1)
    products = ServicesOrders.objects.filter(service__service_user_id=user_id,date__year=date_spilt[0],date__month=date_spilt[1],date__day=date_spilt[2],payment_status=True).order_by('id').all()
    orders = [p.price for p in products]
    return orders