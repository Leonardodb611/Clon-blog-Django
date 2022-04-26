from django.urls import path
from App import views


urlpatterns = [
    
    path("", views.random_blog, name = "inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("create_blog/", views.crear_blog, name="Crear"),
    path("messages", views.mensaje, name = "mensajeria"),
    path("pages", views.leer_blogs, name="leerblogs"),
    path("eliminar/blog/<pk>", views.eliminar_blogs, name="Borrarblog"),
    path("edit/blog/<pk>", views.modificar_blogs, name="Editarblog" ),
    path("pages/<pk>", views.blog_especifico, name="Blogespecifico" ),
    path("edit/profile", views.editar_perfil, name="EditarPerfil"),
    path("profile", views.perfil_usuario, name="Perfil"),
    path("about", views.about, name="About")
    
    

    
]