from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
    
from authentif.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(verbose_name='Email addres', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Name', max_length=255)
    last_name = models.CharField(verbose_name='Surname', max_length=255)
    photo = models.ImageField(verbose_name='Photo', upload_to='users/photos')

    is_active = models.BooleanField(verbose_name= 'activated', default=False)
    is_staff = models.BooleanField(verbose_name= 'staff', default=False)
    is_superuser = models.BooleanField(verbose_name= 'admin', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'  