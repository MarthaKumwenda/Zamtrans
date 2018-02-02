from django.db import models

# Create your models here.
class Local(models.Model):
    route = models.CharField(max_length=30, null=True)
    price = models.CharField(max_length=10)



class City(models.Model):
    company = models.CharField(max_length=30, null=True)
    route = models.CharField(max_length=30, null=True)
    price = models.CharField(max_length=10)
    time = models.TimeField(default=None, null=True)

    class Meta:
        verbose_name_plural='Cities'

class Country(models.Model):
    company = models.CharField(max_length=30, null=True)
    route = models.CharField(max_length=30, null=True)
    price = models.CharField(max_length=10)
    time = models.TimeField(default=None, null=True)

    class Meta:
        verbose_name_plural='Countries'



    