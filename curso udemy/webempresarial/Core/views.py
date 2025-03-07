from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def services(request):
    return render(request, "core/services.html")

def contact(request):
    return render(request, "core/contact.html")

def store(request):
    return render(request, "core/store.html")

def blog(request):
    return render(request, "core/blog.html")

def sample(request):
    return render(request, "core/sample.html")
