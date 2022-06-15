from django.contrib.auth.base_user import BaseUserManager
from extensions.optimization import photo_optimization
from django.contrib.auth.models import AbstractUser
from django.db import models


class manager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(phone, password, **extra_fields)
        return user

    

#  user model with 'phone' as username
class Userperson(AbstractUser):

    gender_choice = [
        ('male', 'male'),
        ('female', "female")
    ]
    roles = [
        ('user', 'user'),
        ('seller', 'seller'),
        ('service', 'service'),
        ('admin', 'admin'),
    ]
    username = None
    fullname = models.CharField(blank=True, null=True,max_length=100, verbose_name="Full Name")
    phone = models.CharField(blank=True, null=True,max_length=20,verbose_name="Phone", unique=True)
    image = models.ImageField(blank=True, null=True,upload_to="userphoto/",verbose_name="User Photo")
    address = models.TextField(null=True,blank=True,verbose_name='Address')
    phone_auth = models.BooleanField(default=False,verbose_name='Phone Auth')
    gender = models.CharField(choices=gender_choice, blank=True, null=True, max_length=50,verbose_name='Gender')
    role = models.CharField(choices=roles,blank=True, null=True, max_length=50,verbose_name='Rols')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')
    is_superuser = models.BooleanField(default=False,blank=True,null=True,verbose_name='Is Super User')
    objects = manager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['fullname']

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Userperson, self).save(*args, **kwargs)




    def __call__(self):
        return f'{self.fullname}'

    def is_staff(self):
        return self.is_superuser
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser


    def __str__(self):
        return f'{self.fullname}'