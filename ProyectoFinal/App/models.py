from django.db import models
import datetime
from django.contrib.auth.models import  User
from ckeditor.fields import RichTextField

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

    
    titulo = models.CharField(max_length=40)

    creador = models.CharField(max_length=40,blank=True)
    contenido = RichTextField()
    creacion = models.DateField(auto_now=True)
    foto = models.ImageField(upload_to="avatars", null=True, blank = True)
    subtitulo = models.CharField(max_length=40)
    

    def __str__(self):

        return f"{self.titulo, self.id, self.creador, self.contenido}"
    
class Mensajerias(models.Model):
    
    remitente = models.CharField(max_length=40)
    destinatario = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500)
    def __str__(self):

        return f"{self.destinatario}-{self.remitente}-{self.contenido}"
    
class RedesSociales(models.Model):
    user = models.OneToOneField(User, to_field="username", on_delete=models.CASCADE)
    facebook = models.CharField(max_length=500, null=True,  blank=True)
    instagram = models.CharField(max_length=500, null=True,  blank=True)
    twitter = models.CharField(max_length=500, null=True,  blank=True)


    def __str__(self):
            return f"{self.user}"