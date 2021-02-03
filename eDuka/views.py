# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from django.views.generic import DetailView


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'all-store/index.html', context)

def product(request, id):

    try:
        products = Product.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()    
    
    return render(request, "all-store/products.html", {"products":products})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.item_set.all()

    else:
        #Create Empty cart for now for none-logged in users
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'all-store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.item_set.all()

    else:
        #Create Empty cart for now for none-logged in users
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'all-store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
