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
                    return render ( request, "Applogin/redireccion_redes.html")

            else:
                return render(request, "Applogin/login.html", {"form":form})

        else:

            return render(request, "Applogin/login.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "Applogin/login.html", {"form":form})

def agregar_avatar(request):
    
    
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

    return render(request, "Applogin/agregar_avatar.html", {"form": formulario})

def borrar_avatar(request):

    usuario = request.user

    avatar = Avatar.objects.get(user=usuario)
    avatar.imagen = "avatars/no-avatar.png"
    avatar.save()

    return redirect ("/")

def agregar_redes(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = RedesSocialesFormulario(request.POST)
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

        miFormulario1 = RedesSocialesFormulario()
    
    return render (request, "Applogin/agregar_redes.html", {"miFormulario1": miFormulario1})
         
def modificar_redes(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    redes = RedesSociales.objects.get(id=pk)

    if request.method == "POST":
        miFormulario = RedesSocialesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            redes.pagina = informacion["pagina"]
            redes.save()
            return redirect ("/")
    else:

        miFormulario = RedesSocialesFormulario(initial={"pagina":redes.pagina,"url": avatares[0].imagen.url})

    return render (request, "Applogin/editar_redes.html", {"miFormulario":miFormulario, "pk":pk, "url": avatares[0].imagen.url})

def eliminar_redes( request, pk):
    
    try:
        redes = RedesSociales.objects.get(id=pk)
        redes.delete()

        return redirect ("/App/profile")
    except Exception as exc:
        return redirect ("/App/profile")

def crear_redes(request):
    
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.method == "POST":

        miFormulario1 = RedesSocialesFormulario(request.POST)
        print(miFormulario1)

        usuario = request.user 
        
        if miFormulario1.is_valid():
            try:
                informacion = miFormulario1.cleaned_data
                redes = RedesSociales(user=usuario, pagina=informacion["pagina"])
                redes.save()
            
                return redirect("/App/profile")
            except:
                
                return redirect("/App/profile")
    else:

        miFormulario1 = RedesSocialesFormulario()
    
    return render (request, "Applogin/agregar_redes.html", {"miFormulario1": miFormulario1})

def cambiar_contrasenia(request):

    if request.method == "POST":
        
        miFormulario = PasswordChangeForm(request.user, request.POST)

        if miFormulario.is_valid():
        
            user = miFormulario.save()

            update_session_auth_hash(request, user)
    
            return redirect ("/")

    else:
        miFormulario = PasswordChangeForm(request.user)

    return render (request, "Applogin/cambiar_pass.html", {"miFormulario":miFormulario})

    
   