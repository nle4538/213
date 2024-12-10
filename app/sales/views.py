from lib2to3.fixes.fix_input import context
from re import template

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.defaultfilters import first

from .form import Sellerform, Customerform
from .models import *


def index(request):
    template = loader.get_template("sales/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))

def seller(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        data = request.POST.get("data")
        u = {'last_name': last_name, 'age': age, 'first_name': first_name, "phone": phone,"email": email, "data": data}
        content = get_context('Пользователь', u)
    else:
        sellerform = Sellerform()
        content = get_context('Пользователь', {"form": sellerform})
    template = loader.get_template("sales/Seller.html")
    return HttpResponse(template.render(content, request))


class CustomerData:
    pass


def customer(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        u = {'last_name': last_name, 'age': age, 'first_name': first_name, "phone": phone,"email": email}
        content = get_context('Пользователь', u)
        u = Customer(request,last_name=last_name, first_name=first_name, age=age, phone=phone, email=email)
        u.save()
    else:
        customerform = Customerform()
        content = get_context('Пользователь', {"form": customerform})
    template = loader.get_template("sales/Customer.html")
    return HttpResponse(template.render(content, request))

def product(request):
    template = loader.get_template("product/index.html")
    context = get_context('')
    return HttpResponse(template.render(context, request))

def get_context(title, d=None):
    context = {'title': title,
               'pages': [('Seller/', 'Продавец'),
                         ('Customer/', 'Покупатель'),
                         ('product/', 'Товар')
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context
