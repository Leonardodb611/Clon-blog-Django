from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
import random
from Applogin.views import *
from django.contrib.auth.models import User
# Create your views here.


def inicio(request):
    return render (request, "App/inicio2.html")



#formulario para crear
def Crear_Blog(request):

    if request.method == "POST":

       miFormulario1 = CrearBlog(request.POST)
       print(miFormulario1)
       if miFormulario1.is_valid():
           informacion = miFormulario1.cleaned_data
           blog = Blog(titulo=informacion['titulo'],creador=informacion['creador'],contenido=informacion['contenido'])
           blog.save()
           return render (request, "App/Gracias_blog.html")

    else:

        miFormulario1 = CrearBlog()
    
    return render (request, "App/crear_Blog.html", {"miFormulario1": miFormulario1})



def crear_Producto(request):
    if request.method == "POST":
        miProducto = Producto(request.POST)
        print(miProducto)
        if miProducto.is_valid():
            informacion = miProducto.cleaned_data
            producto = Productos(producto=informacion['producto'],categoria=informacion['categoria'],precio=informacion['precio'])
            producto.save()
            return render(request, "App/Gracias_producto.html")
    else:
        miProducto = Producto()
    
    return render (request, "App/crear_producto.html", {"miProducto": miProducto})


def usuarioFormulario(request):

    
    if request.method == "POST":

        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                usuario_nuevo = Usuario (nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])

                usuario_nuevo.save()

                return render(request, "App/Gracias_usuario.html")

    else:

        miFormulario = UsuarioFormulario()

        return render(request, "App/formulario.html", {"miFormulario":miFormulario})


def busqueda1(request):
    return render (request, "App/busqueda.html")

def busquedaUsuario(request):
    return render(request, "App/busqueda_usuario.html")


def busqueda(request):

    if request.GET["nombre"]:


        mensaje = "Persona buscada: %r" %request.GET["nombre"]

        nombre1 = request.GET["nombre"]

        nombres = Usuario.objects.filter(nombre__icontains=nombre1)

        return render(request, "App/resultado_usuario.html", {"nombres":nombres, "query":nombre1})

    else:

        mensaje = "no has introducido nada"
        
    return HttpResponse(mensaje)

def busquedaBlog(request):
    return render(request, "App/busqueda_blog.html")

def busquedablog(request):

    if request.GET["prd"]:


        mensaje = "Blog buscado: %r" %request.GET["prd"]

        blog = request.GET["prd"]

        blogs = Blog.objects.filter(titulo__icontains=blog)

        return render(request, "App/resultado_blog.html", {"blogs":blogs, "query":blog})

    else:

        mensaje = "no has introducido nada"
        
    return HttpResponse(mensaje)

def busquedaProducto(request):
    return render(request, "App/busqueda_producto.html")

def busquedaproducto(request):

    if request.GET["producto"]:


        mensaje = "Persona buscada: %r" %request.GET["producto"]

        blog = request.GET["producto"]

        blogs = Productos.objects.filter(producto__icontains=blog)

        return render(request, "App/resultado_ventas.html", {"blogs":blogs, "query":blog})

    else:

        mensaje = "no has introducido nada"
        
    return HttpResponse(mensaje)


def random_blog(request):


    rblog = list(Blog.objects.all())

    if len(rblog) > 3:
        
        
        rblog = random.sample(rblog,4)

        return render (request, "App/inicio.html", {"rblog": rblog[0], "rcreador":rblog[1], "rcontenido":rblog[2], "rcreacion":rblog[3] })

    else:

        
    
        return render(request, "App/inicio2.html")