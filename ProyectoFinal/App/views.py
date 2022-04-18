from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
import random
from Applogin.views import *
from django.contrib.auth.models import User
from django.template import Context
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):

    

    return render (request, "App/inicio2.html",)

#fomulario para crear
def Crear_Blog(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    if request.method == "POST":

        miFormulario1 = CrearBlog(request.POST, request.FILES)
        print(miFormulario1)
        
        
        user = request.user.username
        if miFormulario1.is_valid():
           informacion = miFormulario1.cleaned_data
           blog = Blog(titulo=informacion['titulo'], creador=user, contenido=informacion['contenido'], foto=informacion['foto'])
           
           blog.save()
           
           
           
           return render (request, "App/Gracias_blog.html")

    else:

        miFormulario1 = CrearBlog()
    
    return render (request, "App/crear_Blog.html", {"miFormulario1": miFormulario1 ,"url": avatares[0].imagen.url})

def usuarioFormulario(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    if request.method == "POST":

        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                usuario_nuevo = Usuario (nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])

                usuario_nuevo.save()

                return render(request, "App/Gracias_usuario.html", {"url": avatares[0].imagen.url})

    else:

        miFormulario = UsuarioFormulario()

        return render(request, "App/formulario.html", {"miFormulario":miFormulario,"url": avatares[0].imagen.url})

def random_blog(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)


    rblog = list(Blog.objects.all())
    print(rblog)
    
    if request.user.is_authenticated:
        
        if len(rblog) > 4:
            
            
            rblog = random.sample(rblog,5)

            return render (request, "App/inicio.html", {"rblog": rblog[0], "rcreador":rblog[1], "rcontenido":rblog[2], "rcreacion":rblog[3], "rfoto":rblog[0].foto.url, "url": avatares[0].imagen.url})
            

        else:

        
            return render(request, "App/inicio2.html", {"url": avatares[0].imagen.url})
    
    else:

        if len(rblog) > 4:
            
            
            rblog = random.sample(rblog,5)

            return render (request, "App/inicio.html", {"rblog": rblog[0], "rcreador":rblog[1], "rcontenido":rblog[2],"rfoto":rblog[4],  "rcreacion":rblog[3]})
            

        else:

            
        
            return render(request, "App/inicio2.html")

def mensaje(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    cont_familia = Mensajerias.objects.all()

    cont_familia = Mensajerias.objects.filter(destinatario_id=request.user.username)
    
    print("1",cont_familia)
    print("2", cont_familia)
    
    

    if request.method == "POST":
            
            miFormulario = Mensajeria(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                familiar = Mensajerias (remitente = informacion["remitente"],destinatario_id = informacion["destinatario"],contenido = informacion["contenido"])
                familiar.save()
                return render(request, "App/mensajes.html", {"cont_familia":cont_familia,"url": avatares[0].imagen.url})


        
    else:
            miFormulario = Mensajeria()
        
            return render (request, "App/mensajes.html", {"miFormulario":miFormulario, "cont_familia":cont_familia,"url": avatares[0].imagen.url})

    return  render(request, "App/mensajes.html", {"cont_familia":cont_familia,"url": avatares[0].imagen.url})
        
def leerblogs(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogs = Blog.objects.all()
    
    if request.user.is_authenticated:

        if len(blogs) == 0:
            mensaje = "No hay blogs, disculpe las molestias. Para crear el primero ingrese al sigueinte link."
            return render(request, "App/noBLogs.html", {"mensaje": mensaje, "url": avatares[0].imagen.url})
        else:
            contexto = {"blogs":blogs, "url": avatares[0].imagen.url}

            return render (request, "App/blogs.html", contexto)    
    
    else:

        if len(blogs) == 0:
            mensaje = "No hay blogs, disculpe las molestias. Inicia sesion o crea una cuenta para poder escribir tu blog!"
            return render(request, "App/noBLogs.html", {"mensaje": mensaje})
        else:  
            contexto = {"blogs":blogs}

            return render (request, "App/blogs.html", contexto) 

@login_required
def eliminarblogs( request, pk):
    
    try:
        blogs = Blog.objects.get(id=pk)
        blogs.delete()

        return redirect ("/")
    except Exception as exc:
        return redirect ("/")
@login_required
def modificarBlogs(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogs = Blog.objects.get(id=pk)

    if request.method == "POST":
        miFormulario = CrearBlog(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            blogs.titulo = informacion["titulo"]
            blogs.contenido = informacion["contenido"]
            blogs.foto = informacion["foto"]
        
            blogs.save()

            return redirect ("/")
    else:

        miFormulario = CrearBlog(initial={"titulo":blogs.titulo, "contenido":blogs.contenido, "url": avatares[0].imagen.url})

    return render (request, "App/editarblog.html", {"miFormulario":miFormulario, "pk":pk, "url": avatares[0].imagen.url})

def blogEspecifico(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogs = Blog.objects.get(id=pk)
    
    if request.user.is_authenticated:

        contexto = {"blogs":blogs , "url": avatares[0].imagen.url, "url2": blogs.foto.url}

        return render (request, "App/blogespecifico.html", contexto)
    
    else:

        contexto = {"blogs":blogs}

        return render (request, "App/blogespecifico.html", contexto)

def foto(request):
    
    avatares = Avatar.objects.filter(user_id=request.user.username)
       
    return render(request, "App/padre.html", {"url":avatares[0].imagen.url} )

def editarPerfil(request):

    usuario = request.user

    avatares = Avatar.objects.filter(user_id=request.user.username)

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST)
        

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.password1 = informacion["password1"]
            usuario.passwprd2 = informacion["password2"]
            usuario.save()

            return redirect ("/")
    
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email,"first_name":usuario.first_name, "last_name":usuario.last_name})
        

    return render(request, "App/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario, "url":avatares[0].imagen.url})

def PerfilUsuario(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    usuario = User.objects.get(username=request.user.username)
    redes = RedesSociales.objects.get(user=request.user.username)

    contexto = {"usuario":usuario, "url": avatares[0].imagen.url, "redes":redes}

    

    return render (request, "App/PerfilUsuario.html", contexto)

def AgregarRedes(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = Redessociales(request.POST)
        print(miFormulario1)

        usuario = request.user

        red = RedesSociales.objects.filter(user=usuario)
        
        user = request.user.username
        
        if miFormulario1.is_valid():
           informacion = miFormulario1.cleaned_data
           redes = RedesSociales(user=usuario, facebook=informacion['facebook'], twitter=informacion['twitter'],instagram=informacion['instagram'])
           redes.save()
           
    
           return redirect("/")

    else:

        miFormulario1 = Redessociales()
    
    return render (request, "App/Agregar_redes.html", {"miFormulario1": miFormulario1})

