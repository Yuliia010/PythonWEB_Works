from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home page</h1>")

def news(request):
    return HttpResponse("<h1>News</h1>")

def management(request):
    return HttpResponse("<h1>Management</h1>")

def about(request):
    return HttpResponse("<h1>About the company</h1>")

def contacts(request):
    return HttpResponse("<h1>Contacts</h1>")

def branches(request):
    return HttpResponse("<h1>All branches</h1>")

def location(request, location):
    return HttpResponse(f"<h1>Branch location: {location} </h1>")