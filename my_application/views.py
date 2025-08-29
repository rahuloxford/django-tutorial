from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to home")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("Welcome to about")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("Welcome to contact")
    return render(request, "website/contact.html")

