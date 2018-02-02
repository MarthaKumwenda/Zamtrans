
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Local, City, Country

# Create your views here.
def about(request):
    return render(request, 'web/about.html')

def index(request):
    return render(request, 'web/index.html')

def local(request):
    local = Local.objects.all()
    return render(request, 'web/local.html', {'local': local})

def city(request):
    city = City.objects.all()
    return render(request, 'web/city.html', {'city': city})

def country(request):
    country = Country.objects.all()
    return render(request, 'web/country.html', {'country': country})

