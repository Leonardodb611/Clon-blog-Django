from django.urls import path
from Applogin import views
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login_request, name = "login"),
    path("logout", LogoutView.as_view(template_name="Applogin/gracias.html"), name = "logout"),
    path("Avatar", views.agregarAvatar, name="AgregarAvatar" ),
    path("BorrarAvatar", views.BorrarAvatar, name="BorrarAvatar"),
    path("redes", views.AgregarRedes, name="Redes"),
    path("crearredes", views.crearRedes, name="crearRedes"),
    path("editarRedes/<pk>", views.modificarRedes, name="EditarRedes" ),
    path("eliminarRedes/<pk>", views.eliminarRedes, name="EliminarRedes"),
]