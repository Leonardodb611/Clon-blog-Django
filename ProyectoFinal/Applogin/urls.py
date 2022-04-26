from django.urls import path
from Applogin import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [

    
    path("login", views.login_request, name = "login"),
    path("logout", LogoutView.as_view(template_name="Applogin/gracias_logout.html"), name = "logout"),
    path("Avatar", views.agregar_avatar, name="AgregarAvatar" ),
    path("deleteAvatar", views.borrar_avatar, name="BorrarAvatar"),
    path("redes", views.agregar_redes, name="Redes"),
    path("createRedes", views.crear_redes, name="crearRedes"),
    path("editRedes/<pk>", views.modificar_redes, name="EditarRedes" ),
    path("delRedes/<pk>", views.eliminar_redes, name="EliminarRedes"),
    path("changePassword", views.cambiar_contrasenia, name="resetPass")
]