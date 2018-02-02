
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def about(request):
    return render(request, 'web/about.html')
def index(request):
    return render(request, 'web/index.html')
def map(request):
    return render(request, 'web/map.html')
def index22(request):
    return render(request, 'web/index22.html')
