from django.urls import path
from Applogin import views
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login_request, name = "login"),
    path("logout", LogoutView.as_view(template_name="Applogin/gracias.html"), name = "logout"),
    path("Avatar", views.agregarAvatar, name="AgregarAvatar" )
    
]