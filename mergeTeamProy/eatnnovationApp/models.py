from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
class Meta:
     db_table = 'users'    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)
class Meta:
     db_table = 'products'      


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
class Meta:
     db_table = 'payments' 


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
class Meta:
     db_table = 'inventories'     


class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=50)
class Meta:
     db_table = 'shipments'    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
class Meta:
     db_table = 'reviews'


class Analytic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales = models.IntegerField()
class Meta:
     db_table = 'analytics'   
