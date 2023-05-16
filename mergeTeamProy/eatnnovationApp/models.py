from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        
        if not name:
            raise ValueError('El campo "name" es obligatorio')
        if not email:
            raise ValueError('El campo "email" es obligatorio')
        if not role:
            raise ValueError('El campo "role" es obligatorio')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, email, password, role, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
class Meta:
     db_table = 'users'    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    available = models.IntegerField()
    def __str__(self):
        return self.name
class Meta:
     db_table = 'products'   

class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='DetailBill')
    dateCreation = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return f'Bill {self.id}'  
class Meta:
     db_table = 'bills'         

class DetailBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()     
class Meta:
     db_table = 'DetailsBills'  

class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, default=1)
    datePayment = models.DateTimeField(default=timezone.now)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
class Meta:
     db_table = 'payments' 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,default=1)
    content = models.TextField()
    qualification = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')),default=0)
class Meta:
     db_table = 'reviews'

class Shipment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,default=1)
    address = models.CharField(max_length=200,default=0)
    sendDate= models.DateTimeField(default=datetime.datetime.now)
    sent = models.BooleanField(default=False)
class Meta:
     db_table = 'shipments' 

