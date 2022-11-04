from django.db import models

# Create your models here.

class Project(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    detalles = models.CharField(max_length=200)
    stock = models.IntegerField()
    precios = models.IntegerField()
