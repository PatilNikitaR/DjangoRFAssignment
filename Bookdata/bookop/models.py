from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator



# Create your models here.
class User(AbstractBaseUser):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')
    numeric = RegexValidator(r'^[0-9]*$', 'Only numerics are allowed.')
    # The PermissionsMixin is a mixin for models. The PermissionsMixin [Django-doc] is a mixin for Django models. If you add the mixin to one of your models, it will add fields that are specific for objects that have permissions, like is_superuser , groups , and user_permissions
    # Abstractbaseuser has password, last_login, is_active by default
    # Abstractbaseuser has the authentication functionality only , it has no actual fields you will supply the fields to use when you subclass.
    first_name = models.CharField(max_length=240,default="",validators=[alphanumeric])
    last_name = models.CharField(max_length=255,default="",validators=[alphanumeric])
    # Dob=models.DateField()
    # Age=models.IntegerField()
    email = models.EmailField(unique=True, max_length=254)
    password=models.CharField(max_length=240)
    username=None
    phone = models.CharField(max_length=10, unique=True, default=0,validators=[numeric])
    # address = models.CharField(max_length=250, default="")
    
    
    USERNAME_FIELD= 'email',
    REQUIRED_FIELDS= []
    
    def __str__(self):
        return self.email+ self.password
    
class Book(models.Model):
    
    book_name= models.CharField(max_length=240,unique=True)
    description=models.CharField(max_length=500)
    Author=models.CharField(max_length=240)
    Price=models.IntegerField()
    created_by=models.CharField(max_length=250)
    
    
