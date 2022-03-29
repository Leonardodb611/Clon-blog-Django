from django import forms

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class CrearBlog(forms.Form):

    titulo = forms.CharField(max_length=40)
    creador = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=4000)


class Producto (forms.Form):

    
    producto = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    
    