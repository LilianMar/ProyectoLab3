from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=50)
    def __str__(self):
        return self.name   
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

