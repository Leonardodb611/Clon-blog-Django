from django.db import models
import datetime

# Create your models here.
class Usuario(models.Model):
   
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    password = models.CharField (max_length=12)

class Productos (models.Model):

    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    precio = models.IntegerField()
    

class Administradores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    password = models.CharField (max_length=12)

class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    creador = models.CharField(max_length=40)
    contenido = models.CharField(max_length=1000)
    creacion = models.DateField(auto_now=True)

    def __str__(self):

        return f"{self.titulo}"
    
