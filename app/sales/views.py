import email.utils
from lib2to3.fixes.fix_input import context
from re import template

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import CustomerForm
from django.template import loader
from django.template.defaultfilters import first

from .form import Sellerform, CustomerForm
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

def customer(request):
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                    customer=Customer()
                    customer.first_name = form.fields['first_name']
                    customer.last_name = form.fields['last_name']
                    customer.phone = form.fields['phone']
                    customer.email = form.fields['email']
                    customer.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Создан аккаунт {username}!')
                    return redirect('blog-home')
        else:
            form = CustomerForm()
        return render(request, 'sales/Customer.html', {'form': form})

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