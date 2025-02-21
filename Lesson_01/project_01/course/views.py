from django.shortcuts import render

from django.http import HttpResponse

def laern_django(request):
    return  HttpResponse('Hello Django..!')