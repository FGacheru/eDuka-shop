# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'all-store/index.html', context)

def cart(request):
    context = {}
    return render(request, 'all-store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'all-store/checkout.html', context)