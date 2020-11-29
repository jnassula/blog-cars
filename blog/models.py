from django.conf import settings
from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Fuel(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class Car(models.Model):
    brand = models.ForeignKey('blog.Brand', on_delete=models.CASCADE)
    model = models.ForeignKey('blog.Model', on_delete=models.CASCADE)
    year = models.IntegerField()
    fuel = models.ForeignKey('blog.Fuel', on_delete=models.CASCADE)
    observation = models.TextField()
    national = models.BooleanField()
    tires = models.CharField(max_length=10, null=True, blank=True)  


    def __str__(self):
        return f'{self.brand.name} - {self.model.name}'