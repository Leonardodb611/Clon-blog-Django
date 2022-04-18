from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from App.templates.App import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from Applogin.forms import *
from Applogin.models import *
from django.contrib.auth.decorators import login_required



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
                    return render ( request, "Applogin/nuevoAvatar.html")

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
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
                return render (request, "App/redireccion_redes.html")   
    else:

        formulario = AvatarFormulario()

    return render(request, "Applogin/agregarAvatar.html", {"form": formulario})




               



