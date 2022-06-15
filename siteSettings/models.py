from customizedUserModel.models import Userperson
from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, blank=False, default="some string",verbose_name="Site Name",)
    payment_token = models.CharField(max_length=300, blank = False, default="some string",verbose_name='Payment Token')
    site_description = models.TextField(default="some string",verbose_name='Site Description')
    keyword = models.TextField(default="some string",verbose_name='Keyword')
    logo = models.ImageField(upload_to="logo/v1",verbose_name='Logo')
    contact_number = models.CharField(max_length=15, default='123',verbose_name='Contact number')
    address = models.TextField(null=False, default="some string",verbose_name='Address')
    email = models.EmailField(default='django@mail.com',verbose_name='Email')
    instagram_link = models.URLField(default='instalink',verbose_name="Instagram")
    android_application_link = models.URLField(default="some string",verbose_name="Android Application")
    melipayamak_username = models.CharField(max_length=100,blank=True,null=True,verbose_name='Melipayamak Username')
    melipayamak_password = models.CharField(max_length=100,blank=True,null=True,verbose_name='Melipayamak Password')
    melipayamak_phone = models.CharField(max_length=100,blank=True,null=True,verbose_name='Melipayamak Phone')

    def __str__(self):
        return f'{self.site_name}'



class SocialNetworks(models.Model):
    instagram = models.URLField(verbose_name="Instagram")
    whatsapp = models.URLField(verbose_name="Whatsapp")
    youtube = models.URLField(verbose_name="Youtube")
    telegram = models.URLField(verbose_name="Telegram")
    facebook = models.URLField(verbose_name="Facebook")



class Codes(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='User')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')
    code = models.IntegerField(blank=True,null=True,verbose_name='Code')

    def __str__(self):
        return f'{self.code}'
