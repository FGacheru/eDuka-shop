# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'all-store/index.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []

    context = {'items':items}
    return render(request, 'all-store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'all-store/checkout.html', context)