from django.db import models


# Create your models here.
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
