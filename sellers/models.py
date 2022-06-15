from extensions.optimization import photo_optimization
from extensions.DateJalali import django_jalali
from customizedUserModel.models import Userperson
from django.db import models


# Vendor Categories model
class SellersCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')

    def __str__(self):
        return f'{self.name}'
        

# sellers model
class Sellers(models.Model):
    business_owner = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Business Owner')
    business_name = models.CharField(max_length=999,verbose_name='Business Name')
    business_description = models.TextField(verbose_name='Business Description')
    business_image = models.ImageField(upload_to='Businessimage',blank=False,null=False,verbose_name='Business Image')
    business_license = models.ImageField(upload_to='BusinessLicenseImage',blank=False,null=False,verbose_name='Business License')
    registration_date = models.DateTimeField(auto_now_add=True,verbose_name='Registration Date')
    business_status = models.BooleanField(default=False,verbose_name='business Status')
    business_categories = models.ManyToManyField(SellersCategories,verbose_name='business Categories')

    def save(self, *args, **kwargs):
        photo_optimization(self.business_image)
        photo_optimization(self.business_license)
        super(Sellers, self).save(*args, **kwargs)


    def business_owner_info(self):
        return self.business_owner.fullname

    def business_categories_info(self):
        return [{category.id:category.name} for category in self.business_categories.all()]

    def jdate(self):
        return django_jalali(self.registration_date)

    def __str__(self):
        return f'{self.business_name}'

class SellersUsersMessages(models.Model):
    seller = models.ForeignKey(Sellers,blank=True,null=True,on_delete=models.CASCADE,verbose_name='Seller')
    user = models.ForeignKey(Userperson,blank=False,null=False,on_delete=models.CASCADE,verbose_name='User')

    def user_fullname(self):
        return self.user.fullname

    def user_image(self):
        if self.user.image:
            return self.user.image.url
        else:
            return None

    def seller_fullname(self):
        return self.seller.business_name

    def seller_image(self):
        if self.seller.business_image:
            return self.seller.business_image.url
        else:
            return None

    def __str__(self):
        return f'{self.id}'

class SellersMessages(models.Model):
    seller = models.ForeignKey(Sellers,blank=True,null=True,on_delete=models.CASCADE,verbose_name='Seller')
    user = models.ForeignKey(Userperson,blank=True,null=True,on_delete=models.CASCADE,verbose_name='User')
    text = models.TextField(blank=True,null=True,verbose_name='Text')
    file = models.FileField(upload_to='SellersMessages',blank=True,null=True,verbose_name='File')
    is_seller = models.BooleanField(default=False,verbose_name='Is Seller')

    def __str__(self):
        return f'{self.id}'
        