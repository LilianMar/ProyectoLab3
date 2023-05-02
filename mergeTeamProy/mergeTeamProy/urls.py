"""
URL configuration for mergeTeamProy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from  eatnnovationApp.views import UserList, UserDetail, UserCreate, UserUpdate, UserDelete
from  eatnnovationApp.views import ProductCreate,ProductDelete,ProductDetail,ProductList,ProductUpdate
from  eatnnovationApp.views import ShipmentCreate,ShipmentDelete,ShipmentDetail,ShipmentList,ShipmentUpdate
from  eatnnovationApp.views import ReviewCreate,ReviewDelete,ReviewDetail,ReviewList,ReviewUpdate
from  eatnnovationApp.views import PaymentCreate,PaymentDelete,PaymentDetail,PaymentList,PaymentUpdate
from  eatnnovationApp.views import InventoryCreate,InventoryDelete,InventoryDetail,InventoryList,InventoryUpdate
from  eatnnovationApp.views import AnalyticCreate,AnalyticDelete,AnalyticDetail,AnalyticList,AnalyticUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', TemplateView.as_view(template_name='index.html'), name='home'),

    # La ruta 'leer' en donde listamos todos los registros o Users de la Base de Datos
    path('users/', UserList.as_view(template_name = "users/readUser.html"), name='readUser'),
    # La ruta 'details' en donde mostraremos una página con los details de un Users o registro 
    path('users/detail/<int:pk>', UserDetail.as_view(template_name = "users/detailUser.html"), name='detailUser'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Users o registro  
    path('users/create', UserCreate.as_view(template_name = "users/createUser.html"), name='createUser'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Users o registro de la Base de Datos 
    path('users/edit/<int:pk>', UserUpdate.as_view(template_name = "users/updateUser.html"), name='updateUser'), 
    # La ruta 'delete' que usaremos para delete un Users o registro de la Base de Datos 
    path('users/delete/<int:pk>', UserDelete.as_view(), name='deleteUser'),

    # La ruta 'leer' en donde listamos todos los registros o Products de la Base de Datos
    path('products/', ProductList.as_view(template_name = "products/readProduct.html"), name='readProduct'),
    # La ruta 'details' en donde mostraremos una página con los details de un Products o registro 
    path('products/detail/<int:pk>', ProductDetail.as_view(template_name = "products/detailProduct.html"), name='detailProduct'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Products o registro  
    path('products/create', ProductCreate.as_view(template_name = "products/createProduct.html"), name='createProduct'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Products o registro de la Base de Datos 
    path('products/edit/<int:pk>', ProductUpdate.as_view(template_name = "products/updateProduct.html"), name='updateProduct'), 
    # La ruta 'delete' que usaremos para delete un Products o registro de la Base de Datos 
    path('products/delete/<int:pk>', ProductDelete.as_view(), name='deleteProduct'),

    # La ruta 'leer' en donde listamos todos los registros o Shipments de la Base de Datos
    path('shipments/', ShipmentList.as_view(template_name = "shipments/readShipment.html"), name='readShipment'),
    # La ruta 'details' en donde mostraremos una página con los details de un Shipments o registro 
    path('shipments/detail/<int:pk>', ShipmentDetail.as_view(template_name = "shipments/detailShipment.html"), name='detailShipment'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Shipments o registro  
    path('shipments/create', ShipmentCreate.as_view(template_name = "shipments/createShipment.html"), name='createShipment'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Shipments o registro de la Base de Datos 
    path('shipments/edit/<int:pk>', ShipmentUpdate.as_view(template_name = "shipments/updateShipment.html"), name='updateShipment'), 
    # La ruta 'delete' que usaremos para delete un Shipments o registro de la Base de Datos 
    path('shipments/delete/<int:pk>', ShipmentDelete.as_view(), name='deleteShipment'),

    # La ruta 'leer' en donde listamos todos los registros o Reviews de la Base de Datos
    path('reviews/', ReviewList.as_view(template_name = "reviews/readReview.html"), name='readReview'),
    # La ruta 'details' en donde mostraremos una página con los details de un Reviews o registro 
    path('reviews/detail/<int:pk>', ReviewDetail.as_view(template_name = "reviews/detailReview.html"), name='detailReview'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Reviews o registro  
    path('reviews/create', ReviewCreate.as_view(template_name = "reviews/createReview.html"), name='createReview'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Reviews o registro de la Base de Datos 
    path('reviews/edit/<int:pk>', ReviewUpdate.as_view(template_name = "reviews/updateReview.html"), name='updateReview'), 
    # La ruta 'delete' que usaremos para delete un Reviews o registro de la Base de Datos 
    path('reviews/delete/<int:pk>', ReviewDelete.as_view(), name='deleteReview'),

    # La ruta 'leer' en donde listamos todos los registros o Payments de la Base de Datos
    path('payments/', PaymentList.as_view(template_name = "payments/readPayment.html"), name='readPayment'),
    # La ruta 'details' en donde mostraremos una página con los details de un Payments o registro 
    path('payments/detail/<int:pk>', PaymentDetail.as_view(template_name = "payments/detailPayment.html"), name='detailPayment'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Payments o registro  
    path('payments/create', PaymentCreate.as_view(template_name = "payments/createPayment.html"), name='createPayment'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Payments o registro de la Base de Datos 
    path('payments/edit/<int:pk>', PaymentUpdate.as_view(template_name = "payments/updatePayment.html"), name='updatePayment'), 
    # La ruta 'delete' que usaremos para delete un Payments o registro de la Base de Datos 
    path('payments/delete/<int:pk>', PaymentDelete.as_view(), name='deletePayment'),

    # La ruta 'leer' en donde listamos todos los registros o Inventorys de la Base de Datos
    path('inventories/', InventoryList.as_view(template_name = "inventories/readInventory.html"), name='readInventory'),
    # La ruta 'details' en donde mostraremos una página con los details de un Inventorys o registro 
    path('inventories/detail/<int:pk>', InventoryDetail.as_view(template_name = "inventories/detailInventory.html"), name='detailInventory'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Inventorys o registro  
    path('inventories/create', InventoryCreate.as_view(template_name = "inventories/createInventory.html"), name='createInventory'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Inventorys o registro de la Base de Datos 
    path('inventories/edit/<int:pk>', InventoryUpdate.as_view(template_name = "inventories/updateInventory.html"), name='updateInventory'), 
    # La ruta 'delete' que usaremos para delete un Inventorys o registro de la Base de Datos 
    path('inventories/delete/<int:pk>', InventoryDelete.as_view(), name='deleteInventory'),

    # La ruta 'leer' en donde listamos todos los registros o Analytics de la Base de Datos
    path('analitics/', AnalyticList.as_view(template_name = "analitics/readAnalytic.html"), name='readAnalytic'),
    # La ruta 'details' en donde mostraremos una página con los details de un Analytics o registro 
    path('analitics/detail/<int:pk>', AnalyticDetail.as_view(template_name = "analitics/detailAnalytic.html"), name='detailAnalytic'),
    # La ruta 'create' en donde mostraremos un formulario para create un nuevo Analytics o registro  
    path('analitics/create', AnalyticCreate.as_view(template_name = "analitics/createAnalytic.html"), name='createAnalytic'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Analytics o registro de la Base de Datos 
    path('analitics/edit/<int:pk>', AnalyticUpdate.as_view(template_name = "analitics/updateAnalytic.html"), name='updateAnalytic'), 
    # La ruta 'delete' que usaremos para delete un Analytics o registro de la Base de Datos 
    path('analitics/delete/<int:pk>', AnalyticDelete.as_view(), name='deleteAnalytic'),

] 
