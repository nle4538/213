from django import forms
from django.templatetags.i18n import language
from django.utils.regex_helper import Choice

class Sellerform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=15)
    age = forms.CharField(max_length=15)
    data = forms.DateTimeField()
    email = forms.EmailField()

class Customerform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
#class product(forms.Form):
