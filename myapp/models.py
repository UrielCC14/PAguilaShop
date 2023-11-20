from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    temporada = models.CharField(max_length=200,default='temporada')
    description = models.TextField()
    price = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos', null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Shipping_Address(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.address
    
class Targets(models.Model):
    target_number = models.CharField(max_length=200)
    target_name= models.CharField(max_length=200)
    cvv = models.CharField(max_length=200)
    expiration_date = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.target_name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Shipping_Address, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=200, null=True)
    payment_method = models.ForeignKey(Targets, on_delete=models.SET_NULL,null=True)
    specifications = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return self.product.name
    
class Zona(models.Model):
    nombre = models.CharField(max_length=200,unique=True)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(upload_to='zones',null=True)
    
    def __str__(self):
        return self.nombre

class Tickets(models.Model):
    zona = models.ForeignKey(Zona,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    Precio = models.CharField(max_length=200)
    comprado = models.BooleanField(default=False)
    
    def  __str__(self):
        return f'{self.name} + {self.zona}'
    
class Sale_Tickets(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Targets, on_delete=models.SET_NULL,null=True)
    contact_number = models.CharField(max_length=200, null=True)
    total = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ticket.name