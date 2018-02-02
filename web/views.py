
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def about(request):
    return render(request, 'web/about.html')
def index(request):
    return render(request, 'web/index.html')
