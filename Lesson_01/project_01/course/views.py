from django.shortcuts import render

from django.http import HttpResponse

def learn_django(request):
    return  HttpResponse('<h1>Hello Django..!</h1>')


def learn_python(request):
    return  HttpResponse('<h1>Hello Python..!</h1>')