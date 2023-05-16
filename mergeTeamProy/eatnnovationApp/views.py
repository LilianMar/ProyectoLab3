from django.shortcuts import render

# Create your views here.

from .models import Product, User, Bill,DetailBill, Shipment, Review, Payment

#Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
#Habilitamos el uso de mensajes en Django 
from django.contrib import messages
#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin
#Habilitamos los formularios en Django 
from django import forms

# Create your views here.

class ProductList(ListView):
    model = Product 

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py'
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Product
    def get_success_url(self):        
        return reverse('readProduct') # revisar la pagina a la que se va a redireccionar User 
      
class ProductDetail(DetailView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product # Llamamos a la clase 'Product' que se encuentra en nuestro archivo 'models.py' 
    form = Product # Definimos nuestro formulario con el nombre de la clase o modelo 'Product' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'products' de nuestra Base de Datos 
    success_message = 'Product Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Product 

    # Redireccionamos a la página principal luego de actualizar un registro o Product
    def get_success_url(self):               
        return reverse('readProduct') # Redireccionamos a la vista principal 'leer'

class ProductDelete(SuccessMessageMixin, DeleteView): 
    model = Product 
    form = Product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Product
    def get_success_url(self): 
        success_message = 'Product deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Product 
        messages.success (self.request, (success_message))       
        return reverse('readProduct') # Redireccionamos a la vista principal 'leer'  
    


class UserList(ListView):
    model = User 

class UserCreate(SuccessMessageMixin, CreateView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py'
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo User
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla users de nuestra Base de Datos 
    success_message = 'User Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o User
    def get_success_url(self):        
        return reverse('readUser') 
      
class UserDetail(DetailView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py' 

class UserUpdate(SuccessMessageMixin, UpdateView): 
    model = User # Llamamos a la clase User que se encuentra en nuestro archivo 'models.py' 
    form = User # Definimos nuestro formulario con el nombre de la clase o modelo User 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla users de nuestra Base de Datos 
    success_message = 'User Updated Succesfully !' # Mostramos este Mensaje luego de Editar un User 

    # Redireccionamos a la página principal luego de actualizar un registro o User
    def get_success_url(self):               
        return reverse('readUser') # Redireccionamos a la vista principal 'leer'

class UserDelete(SuccessMessageMixin, DeleteView): 
    model = User 
    form = User
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o User
    def get_success_url(self): 
        success_message = 'User deleted Succesfully !' # Mostramos este Mensaje luego de Editar un User 
        messages.success (self.request, (success_message))       
        return reverse('readUser') # Redireccionamos a la vista principal 'leer'  
    


class ShipmentList(ListView):
    model = Shipment 

class ShipmentCreate(SuccessMessageMixin, CreateView): 
    model = Shipment # Llamamos a la clase Shipment que se encuentra en nuestro archivo 'models.py'
    form = Shipment # Definimos nuestro formulario con el nombre de la clase o modelo Shipment
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla shipments de nuestra Base de Datos 
    success_message = ' Shipment Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Shipment
    def get_success_url(self):        
        return reverse('readShipment') 
      
class ShipmentDetail(DetailView): 
    model = Shipment # Llamamos a la clase Shipment que se encuentra en nuestro archivo 'models.py' 

class ShipmentUpdate(SuccessMessageMixin, UpdateView): 
    model = Shipment # Llamamos a la clase Shipment que se encuentra en nuestro archivo 'models.py' 
    form = Shipment # Definimos nuestro formulario con el nombre de la clase o modelo Shipment 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla shipments de nuestra Base de Datos 
    success_message = ' Shipment Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Shipment 

    # Redireccionamos a la página principal luego de actualizar un registro o Shipment
    def get_success_url(self):               
        return reverse('readShipment') # Redireccionamos a la vista principal 'leer'

class ShipmentDelete(SuccessMessageMixin, DeleteView): 
    model = Shipment 
    form = Shipment
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Shipment
    def get_success_url(self): 
        success_message =' Shipment deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Shipment 
        messages.success (self.request, (success_message))       
        return reverse('readShipment') # Redireccionamos a la vista principal 'leer'  


class ReviewList(ListView):
    model = Review 

class ReviewCreate(SuccessMessageMixin, CreateView): 
    model = Review # Llamamos a la clase Review que se encuentra en nuestro archivo 'models.py'
    form = Review # Definimos nuestro formulario con el nombre de la clase o modelo Review
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla reviews de nuestra Base de Datos 
    success_message = ' Review Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Review
    def get_success_url(self):        
        return reverse('readReview') 
      
class ReviewDetail(DetailView): 
    model = Review # Llamamos a la clase Review que se encuentra en nuestro archivo 'models.py' 

class ReviewUpdate(SuccessMessageMixin, UpdateView): 
    model = Review # Llamamos a la clase Review que se encuentra en nuestro archivo 'models.py' 
    form = Review # Definimos nuestro formulario con el nombre de la clase o modelo Review 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla reviews de nuestra Base de Datos 
    success_message = ' Review Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Review 

    # Redireccionamos a la página principal luego de actualizar un registro o Review
    def get_success_url(self):               
        return reverse('readReview') # Redireccionamos a la vista principal 'leer'

class ReviewDelete(SuccessMessageMixin, DeleteView): 
    model = Review 
    form = Review
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Review
    def get_success_url(self): 
        success_message =' Review deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Review 
        messages.success (self.request, (success_message))       
        return reverse('readReview') # Redireccionamos a la vista principal 'leer'  
    

class PaymentList(ListView):
    model = Payment 

class PaymentCreate(SuccessMessageMixin, CreateView): 
    model = Payment # Llamamos a la clase Payment que se encuentra en nuestro archivo 'models.py'
    form = Payment # Definimos nuestro formulario con el nombre de la clase o modelo Payment
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla payments de nuestra Base de Datos 
    success_message = ' Payment Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Payment
    def get_success_url(self):        
        return reverse('readPayment') 
      
class PaymentDetail(DetailView): 
    model = Payment # Llamamos a la clase Payment que se encuentra en nuestro archivo 'models.py' 

class PaymentUpdate(SuccessMessageMixin, UpdateView): 
    model = Payment # Llamamos a la clase Payment que se encuentra en nuestro archivo 'models.py' 
    form = Payment # Definimos nuestro formulario con el nombre de la clase o modelo Payment 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla payments de nuestra Base de Datos 
    success_message = ' Payment Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Payment 

    # Redireccionamos a la página principal luego de actualizar un registro o Payment
    def get_success_url(self):               
        return reverse('readPayment') # Redireccionamos a la vista principal 'leer'

class PaymentDelete(SuccessMessageMixin, DeleteView): 
    model = Payment 
    form = Payment
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Payment
    def get_success_url(self): 
        success_message =' Payment deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Payment 
        messages.success (self.request, (success_message))       
        return reverse('readPayment') # Redireccionamos a la vista principal 'leer'  
    

class BillList(ListView):
    model = Bill 

class BillCreate(SuccessMessageMixin, CreateView): 
    model = Bill # Llamamos a la clase Bill que se encuentra en nuestro archivo 'models.py'
    form = Bill # Definimos nuestro formulario con el nombre de la clase o modelo Bill
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla inventories de nuestra Base de Datos 
    success_message = ' Bill Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o Bill
    def get_success_url(self):        
        return reverse('readBill') 
      
class BillDetail(DetailView): 
    model = Bill # Llamamos a la clase Bill que se encuentra en nuestro archivo 'models.py' 

class BillUpdate(SuccessMessageMixin, UpdateView): 
    model = Bill # Llamamos a la clase Bill que se encuentra en nuestro archivo 'models.py' 
    form = Bill # Definimos nuestro formulario con el nombre de la clase o modelo Bill 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla inventories de nuestra Base de Datos 
    success_message = ' Bill Updated Succesfully !' # Mostramos este Mensaje luego de Editar un Bill 

    # Redireccionamos a la página principal luego de actualizar un registro o Bill
    def get_success_url(self):               
        return reverse('readBill') # Redireccionamos a la vista principal 'leer'

class BillDelete(SuccessMessageMixin, DeleteView): 
    model = Bill 
    form = Bill
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Bill
    def get_success_url(self): 
        success_message =' Bill deleted Succesfully !' # Mostramos este Mensaje luego de Editar un Bill 
        messages.success (self.request, (success_message))       
        return reverse('readBill') # Redireccionamos a la vista principal 'leer'  
    

class DetailBillList(ListView):
    model = DetailBill 

class DetailBillCreate(SuccessMessageMixin, CreateView): 
    model = DetailBill # Llamamos a la clase DetailBill que se encuentra en nuestro archivo 'models.py'
    form = DetailBill # Definimos nuestro formulario con el nombre de la clase o modelo DetailBill
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla DetailBill de nuestra Base de Datos 
    success_message = ' Detail Bill Created Succesfully!' # Mostramos este Mensaje luego de Crear un Product

    # Redireccionamos a la página principal luego de crear un registro o DetailBill
    def get_success_url(self):        
        return reverse('readDetailBill') 
      
class DetailBillDetail(DetailView): 
    model = DetailBill # Llamamos a la clase DetailBill que se encuentra en nuestro archivo 'models.py' 

class DetailBillUpdate(SuccessMessageMixin, UpdateView): 
    model = DetailBill # Llamamos a la clase DetailBill que se encuentra en nuestro archivo 'models.py' 
    form = DetailBill # Definimos nuestro formulario con el nombre de la clase o modelo DetailBill 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla DetailBill de nuestra Base de Datos 
    success_message = ' Detail Bill Updated Succesfully !' # Mostramos este Mensaje luego de Editar un DetailBill 

    # Redireccionamos a la página principal luego de actualizar un registro o DetailBill
    def get_success_url(self):               
        return reverse('readDetailBill') # Redireccionamos a la vista principal 'leer'

class DetailBillDelete(SuccessMessageMixin, DeleteView): 
    model = DetailBill 
    form = DetailBill
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o DetailBill
    def get_success_url(self): 
        success_message =' Detail Bill deleted Succesfully !' # Mostramos este Mensaje luego de Editar un DetailBill 
        messages.success (self.request, (success_message))       
        return reverse('readDetailBill') # Redireccionamos a la vista principal 'leer'  
