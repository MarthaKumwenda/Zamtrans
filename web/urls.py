from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^index$', views.index, name='index'),
url(r'^about$', views.about, name='about'),
url(r'^local$', views.local, name='local'),
url(r'^city$', views.city, name='city'),
url(r'^country$', views.country, name='country'),
]
