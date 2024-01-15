from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return HttpResponse("Landing page")

def about(request):
    return HttpResponse("About us")

def register(request):
    return HttpResponse("Register")

def login(request):
    return HttpResponse("Login")


# Create your views here.
