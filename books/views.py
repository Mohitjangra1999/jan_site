from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1>Anshu jangra tu chutiye hai </h1>")

def new_fun(request):
    return HttpResponse("<h1>This is new homepage</h1>")