from django.urls import path
from Applogin import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [

    
    path("login", views.login_request, name = "login"),
    path("logout", LogoutView.as_view(template_name="Applogin/gracias.html"), name = "logout"),
    path("Avatar", views.agregarAvatar, name="AgregarAvatar" ),
    path("deleteAvatar", views.BorrarAvatar, name="BorrarAvatar"),
    path("redes", views.AgregarRedes, name="Redes"),
    path("createRedes", views.crearRedes, name="crearRedes"),
    path("editRedes/<pk>", views.modificarRedes, name="EditarRedes" ),
    path("delRedes/<pk>", views.eliminarRedes, name="EliminarRedes"),
    path("changePassword", views.cambiarContrasenia, name="resetPass")
]