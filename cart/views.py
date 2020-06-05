from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        print("okay")
        return render(request, "user/index.html", {"message": None})
    cart_items = Cart_Item.objects.filter(cart__user = request.user)
    print(Cart_Item.objects.filter(cart__user = request.user))
    context = {
        "user": request.user,
        "cart_items": Cart_Item.objects.filter(cart__user = request.user)
    }
    return render(request, "cart/cart.html", context)


def cart_item(request, item):
    if not request.user.is_authenticated:
        print("okay")
        messages.error(request, "Please login first to add to cart.")
        return JsonResponse({"success": False})

    stuff = json.loads(item)
    print(stuff)
    
    try:
        cart = Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user = request.user)
 
    if stuff["toppings"] == "" or stuff["toppings"] == "":
        product = Product.objects.create(name = stuff["item_name"], size = stuff["size"], price = stuff["price"], category = Category.objects.get(menu__id = stuff["category"]))
        cart_item = Cart_Item.objects.create(product = product, quantity = stuff["quantity"], cart = cart)
    
    if stuff["toppings"] != "":
        toppings = []
        for top in stuff["toppings"]:
            toppings.append(Toppings.objects.get(topping = top))
            add = Additional.objects.create(toppings = Toppings.objects.get(topping = top) )
            product = Product.objects.create(name = stuff["item_name"], size = stuff["size"], price = stuff["price"], category = Category.objects.get(menu__id = stuff["category"]), additionals = add)
            cart_item = Cart_Item.objects.create(product = product, quantity = stuff["quantity"], cart = cart)
         

    if stuff["extra"] != "":
        extra = []
        for ext in stuff["extra"]:
            add = Additional.objects.create(extra = Extra.objects.get(extra = ext) )
            product = Product.objects.create(name = stuff["item_name"], size = stuff["size"], price = stuff["price"], category = Category.objects.get(menu__id = stuff["category"]), additionals = add)
            cart_item = Cart_Item.objects.create(product = product, quantity = stuff["quantity"], cart = cart)
    
    return JsonResponse({"success": True})