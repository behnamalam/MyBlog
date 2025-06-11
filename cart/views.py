from django.shortcuts import render,HttpResponse,get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse
import json


# Create your views here.

def cart_summary(request):
    return render(request,"cart/index.html")

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == "post": # get one data of ajax

        # get id from ajax
        product_id = request.POST.get("product_id")

        # check if product exist or not in database
        product = get_object_or_404(Product,id=product_id)

        # add to session key 
        cart.add(product=product)

        # create a json file for initialize session
        response = JsonResponse({"product_name" : product.name})


        return response





def cart_delete(request):
    return HttpResponse("delete")

def cart_update(request):
    return HttpResponse("update")