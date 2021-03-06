from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from orders.models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs, Pastas, DinnerPlatters, Salads, Menu, Extra

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.menu}"

class Additional(models.Model):
    additional = models.BooleanField(default = False)
    toppings = models.ManyToManyField(Toppings, null = True, blank = True )
    extra = models.ManyToManyField(Extra, null = True, blank = True )

    def __str__(self):
        return f"{self.toppings}, {self.extra}"

class Product(models.Model):
    name = models.CharField( max_length = 20 )
    size =  models.CharField( max_length = 20, null = True, blank = True )
    price = models.DecimalField( max_digits = 10, decimal_places = 2 )
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    additional = models.ForeignKey(Additional, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"${self.price}, {self.name}, {self.size}, {self.category}"

class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.cart}"

class Order_Items(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True)
    quantity = models.PositiveSmallIntegerField(default = 1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.cart}"

class Order(models.Model):
    order_items = models.ForeignKey(Order_Items, on_delete=models.CASCADE)
    total = models.DecimalField( max_digits = 10, decimal_places = 2 )

    def __str__(self):
        return f"{self.order_items}, {self.total}"