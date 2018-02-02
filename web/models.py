from django.db import models

# Create your models here.
class Local(models.Model):
    destination = models.CharField(max_length=30, null=True)
    price = models.IntegerField(max_length=10)