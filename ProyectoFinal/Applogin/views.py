from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from App.templates.App import *
from django.shortcuts import redirect
from django.contrib.auth.models import User




# Create your views here.
def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario = form.cleaned_data["username"]
            form.save()
            return redirect("/")


    else:
        form = UserCreationForm()

    return render(request, "Applogin/registro.html", {"form":form})



def login_request (request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return redirect("/")

            else:
                return render(request, "Applogin/gracias.html", {"mensaje":"error"})

        else:

            return render(request, "Applogin/gracias.html", {"mensaje":"error"})

    form = AuthenticationForm()

    return render(request, "Applogin/login.html", {"form":form})











