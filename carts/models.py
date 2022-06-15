from products.models import Products,ProductsSizes,ProductsColors
from customizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from sellers.models import Sellers
from django.db import models

class Carts(models.Model):
    user = models.ForeignKey(Userperson, on_delete=models.CASCADE, verbose_name='Shoper')
    payment_date = models.DateTimeField(auto_now_add=True,blank=True,null=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def jdate(self):
        return django_jalali(self.payment_date)


    def __str__(self):
        return f'{self.user}'


class Orders(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE,blank=True,null=True,verbose_name='Cart')
    title = models.CharField(blank=True,null=True,max_length=999, verbose_name='Title')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    price = models.IntegerField(blank=True, null=True, verbose_name='Price')
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE,blank=True,null=True, verbose_name='Seller')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=False, null=False, verbose_name='Product ')
    size = models.ForeignKey(ProductsSizes,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Size')
    color = models.ForeignKey(ProductsColors,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Color')
    count = models.IntegerField(default=1,blank=True,null=True,verbose_name='Count')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def jdate(self):
        return django_jalali(self.payment_date)

    def __str__(self):
        return f'{self.title}'