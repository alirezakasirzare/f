from siteSettings.models import SiteSettings
from .melipayamak import Api

#  50004001666144
# 09130666144
# 831#6d4fO
def send_sms(phone,text):
    settings: SiteSettings = SiteSettings.objects.first()
    username = f'{settings.melipayamak_username}'
    password = f'{settings.melipayamak_password}'
    api = Api(username,password)
    sms = api.sms()
    to = f'{phone}'
    _from = f'{settings.melipayamak_phone}'
    text = f'{text}'
    response = sms.send(to,_from,text)
    return "OK"
