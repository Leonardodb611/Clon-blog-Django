from django.urls import path
from Applogin import views

urlpatterns = [

    path("register", views.register, name="register"),
    path("login", views.login_request, name = "login")
]