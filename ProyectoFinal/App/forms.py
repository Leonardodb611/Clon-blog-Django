from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class CrearBlog(forms.Form):

    titulo = forms.CharField(max_length=40)
   
    contenido = forms.CharField(max_length=4000)
    foto = forms.ImageField()
    

class Mensajeria(forms.Form):
    
    remitente = forms.CharField(max_length=40)
    destinatario = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=500)
     
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

class Redessociales(forms.Form):
    facebook = forms.CharField()
    instagram = forms.CharField()
    twitter = forms.CharField()