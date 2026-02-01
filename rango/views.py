from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/about'> link</a>")

def about(request):
    return HttpResponse("Rango says here is the about page <a href='/'> home</a>")