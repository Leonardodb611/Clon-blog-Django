from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="modificar email")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="introducir su primer nombre")
    last_name = forms.CharField(label="introducir su primer nombre")
    



    class Meta: 
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_text = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

