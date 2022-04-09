from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from App.templates.App import *
from django.shortcuts import redirect



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

