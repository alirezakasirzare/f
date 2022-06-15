from extensions.optimization import photo_optimization
from customizedUserModel.models import Userperson
from extensions.DateJalali import django_jalali
from django.db import models
import datetime


# Service categoies model
class ServicesCategories(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class ServicesCompanies(models.Model):
    name = models.CharField(max_length=999,verbose_name='Name')
    management = models.CharField(max_length=999,verbose_name='Management')
    established_year = models.CharField(max_length=999,verbose_name='Established Year')
    address = models.CharField(max_length=999,verbose_name='Address')

    def __str__(self):
        return f'{self.name}'

# Service model
class Services(models.Model):
    service_user = models.ForeignKey(Userperson,on_delete=models.CASCADE,null=True,blank=True,verbose_name='service user')
    title = models.CharField(max_length=999,verbose_name='Title service')
    company = models.ForeignKey(ServicesCompanies,on_delete=models.CASCADE,verbose_name='Company')
    image = models.ImageField(upload_to='services',verbose_name='Image')
    description = models.TextField(verbose_name='Description')
    short_description = models.TextField(verbose_name='Description')
    categories = models.ManyToManyField(ServicesCategories,verbose_name='Categories')
    score = models.IntegerField(default=1,blank=False,null=False,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Services, self).save(*args, **kwargs)

    def service_user_fullname(self):
        return self.service_user.fullname

    def service_user_gender(self):
        return self.service_user.gender

    def service_reservations(self):
        reservations = ServicesCollaborationHours.objects.filter(service_user_id=self.id).all()
        return [r.hour for r in reservations]
    
    
    def company_info(self):
        return [{'name': self.company.name},{'management': self.company.management},{'established_year': self.company.established_year},{'address': self.company.address}]

    def jdate(self):
        return django_jalali(self.date)

    def __str__(self):
        return f'{self.title}'




class ServicesCollaborationHours(models.Model):
    service_user = models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name='Service User',related_name='service_reservation')
    hour = models.CharField(max_length=999,blank=True,null=True,verbose_name='Hours')

    def __str__(self):
        return f'{self.hour}'





class ServicesSliders(models.Model):
    image = models.ImageField(upload_to='ServicesSliders',verbose_name='Image')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(ServicesSliders, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.url


class ServicesComments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,null=True,blank=True,verbose_name='User')
    service = models.ForeignKey(Services,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Service Id')
    comment = models.TextField(null=False,blank=False,verbose_name='Comment')
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True, verbose_name='Date')
    status = models.BooleanField(null=True,blank=True,default=False,verbose_name='Status')


    def user_image(self):
        if self.user.image:
            return self.user.image.url
        else:
            return None

    def user_fullname(self):
        return self.user.fullname


    def scores(self):
        scores = ServicesScores.objects.filter(user_id=self.user.id,service_id=self.service.id).first()
        if scores is not None:
            return scores.score
        else:
            return None



    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user}'


class ServicesScores(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,null=True,blank=True,verbose_name='User')
    service = models.ForeignKey(Services, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Service Id')
    score = models.IntegerField(blank=False,null=False,verbose_name='Score')
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True, verbose_name='Date')


    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user}'


class ServicesOrders(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,null=True,blank=True,verbose_name='User')
    service = models.ForeignKey(Services, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Service Id')
    price = models.IntegerField(blank=False,null=False,verbose_name='Price')
    payment_status = models.BooleanField(default=False,verbose_name='Payment status')
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True, verbose_name='Date')

    def user_fullname(self):
        return self.user.fullname


    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user}'


class ServicesComplaints(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,null=True,blank=True,verbose_name='User')
    service = models.ForeignKey(Services,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Service')
    text = models.TextField(verbose_name='Text')
    date = models.DateTimeField(auto_now_add=True)

    def jdate(self):
        return django_jalali(self.date)

    def __str__(self):
        return f'{self.text[:50]}...'


class ServicesUsersMessages(models.Model):
    service = models.ForeignKey(Services, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Service')
    user = models.ForeignKey(Userperson, blank=False, null=False, on_delete=models.CASCADE, verbose_name='User')

    def user_fullname(self):
        return self.user.fullname

    def user_image(self):
        if self.user.image:
            return self.user.image.url
        else:
            return None

    def service_fullname(self):
        return self.service.title

    def service_image(self):
        if self.service.image:
            return self.service.image.url
        else:
            return None

    def __str__(self):
        return f'{self.id}'


class ServicesMessages(models.Model):
    service = models.ForeignKey(Services, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Service')
    user = models.ForeignKey(Userperson, blank=True, null=True, on_delete=models.CASCADE, verbose_name='User')
    text = models.TextField(blank=True, null=True, verbose_name='Text')
    file = models.FileField(upload_to='ServicesMessages', blank=True, null=True, verbose_name='File')
    is_service = models.BooleanField(default=False, verbose_name='Is Service')

    def __str__(self):
        return f'{self.id}'
