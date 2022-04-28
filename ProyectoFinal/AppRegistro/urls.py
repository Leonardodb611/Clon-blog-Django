from django.urls import path
from AppRegistro import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path("register", views.register, name="Register"),
    
]