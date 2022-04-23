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
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.



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

        miFormulario1 = RedessocialesForm(request.POST)
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

        miFormulario1 = RedessocialesForm()
    
    return render (request, "App/Agregar_redes.html", {"miFormulario1": miFormulario1})
         
def modificarRedes(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    redes = RedesSociales.objects.get(id=pk)

    if request.method == "POST":
        miFormulario = RedessocialesForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            redes.pagina = informacion["pagina"]
            redes.save()
            return redirect ("/")
    else:

        miFormulario = RedessocialesForm(initial={"pagina":redes.pagina,"url": avatares[0].imagen.url})

    return render (request, "Applogin/editarRedes.html", {"miFormulario":miFormulario, "pk":pk, "url": avatares[0].imagen.url})

def eliminarRedes( request, pk):
    
    try:
        redes = RedesSociales.objects.get(id=pk)
        redes.delete()

        return redirect ("/App/profile")
    except Exception as exc:
        return redirect ("/App/profile")

def crearRedes(request):
    
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = RedessocialesForm(request.POST)
        print(miFormulario1)

        usuario = request.user 
        
        if miFormulario1.is_valid():
            informacion = miFormulario1.cleaned_data
            redes = RedesSociales(user=usuario, pagina=informacion["pagina"])
            redes.save()
           
            return redirect("/App/profile")
        
    else:

        miFormulario1 = RedessocialesForm()
    
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

    
   