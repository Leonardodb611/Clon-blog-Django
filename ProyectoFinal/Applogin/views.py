from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from App.templates.App import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from Applogin.forms import *
from Applogin.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            
            form.save()
            
            return redirect ("/")


    else:
        form = UserRegisterForm()

    return render(request, "Applogin/registro.html", {"form":form})



def login_request (request):
    
    error = "datos erroneos"
    

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:

                avatar = Avatar.objects.filter(user=usuario)
                
                if len(avatar) > 0:

                    login(request, user)

                    return redirect("/")

                else:
                    login(request, user)
                    return render ( request, "App/redireccion_redes.html")

            else:
                return render(request, "Applogin/login.html", {"form":form})

        else:

            return render(request, "Applogin/login.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "Applogin/login.html", {"form":form})

def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST)
        miFormulario2 = AvatarFormulario(request.POST, request.FILES)

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
        miFormulario = UserEditForm(initial={"email":usuario.email})
        miFormulario2 = AvatarFormulario()

    return render(request, "App/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def agregarAvatar(request):
    
    
    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
                return redirect("/")

            else:
                avatar = Avatar(user=usuario, imagen="avatars/no-avatar.png")
                avatar.save()
            
                return render (request, "App/redireccion_redes.html")   
    else:

        formulario = AvatarFormulario()

    return render(request, "Applogin/agregarAvatar.html", {"form": formulario})

def BorrarAvatar(request):

    usuario = request.user

    avatar = Avatar.objects.get(user=usuario)
    avatar.imagen = "avatars/no-avatar.png"
    avatar.save()

    return redirect ("/")


def AgregarRedes(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = Redessociales(request.POST)
        print(miFormulario1)

        usuario = request.user

        
        
        user = request.user.username
        
        if miFormulario1.is_valid():
           informacion = miFormulario1.cleaned_data
           redes = RedesSociales(user=usuario, pagina=informacion["pagina"])
           redes.save()
           avatar = Avatar(user=usuario, imagen="avatars/no-avatar.png")
           avatar.save()
           return redirect("/")

    else:

        miFormulario1 = Redessociales()
    
    return render (request, "App/Agregar_redes.html", {"miFormulario1": miFormulario1})
         
def modificarRedes(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    redes = RedesSociales.objects.get(id=pk)

    if request.method == "POST":
        miFormulario = Redessociales(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            redes.pagina = informacion["pagina"]
            redes.save()
            return redirect ("/")
    else:

        miFormulario = Redessociales(initial={"pagina":redes.pagina,"url": avatares[0].imagen.url})

    return render (request, "Applogin/editarRedes.html", {"miFormulario":miFormulario, "pk":pk, "url": avatares[0].imagen.url})

def eliminarRedes( request, pk):
    
    try:
        redes = RedesSociales.objects.get(id=pk)
        redes.delete()

        return redirect ("/App/perfil")
    except Exception as exc:
        return redirect ("/App/perfil")

def crearRedes(request):
    
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = Redessociales(request.POST)
        print(miFormulario1)

        usuario = request.user 
        try:
            if miFormulario1.is_valid():
                informacion = miFormulario1.cleaned_data
                redes = RedesSociales(user=usuario, pagina=informacion["pagina"])
                redes.save()
                return redirect("/App/perfil")
        except:
            
            return redirect("/App/perfil")
    else:

        miFormulario1 = Redessociales()
    
    return render (request, "App/Agregar_redes.html", {"miFormulario1": miFormulario1})

def cambiarContrasenia(request):

    if request.method == "POST":
        
        miFormulario = PasswordReset(request.user, request.POST)

        if miFormulario.is_valid():
        
            user = miFormulario.save()

            update_session_auth_hash(request, user)
    
            return redirect ("/")

    else:
        miFormulario = PasswordReset(request.user)

    return render (request, "Applogin/cambiarPass.html", {"miFormulario":miFormulario})

    
   