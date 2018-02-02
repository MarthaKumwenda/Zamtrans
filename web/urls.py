from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^index$', views.index, name='index'),
url(r'^about$', views.about, name='about'),
]
