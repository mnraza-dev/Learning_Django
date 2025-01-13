from django.shortcuts import render


def aboutpage (request):
    return render(request, 'about.html')


def homepage (request):
    return render(request, 'home.html')