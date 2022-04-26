from django.urls import path
from App import views


urlpatterns = [
    
    path("", views.random_blog, name = "inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("createBlog/", views.crear_blog, name="Crear"),
    path("messages", views.mensaje, name = "mensajeria"),
    path("pages", views.leer_blogs, name="leerblogs"),
    path("eliminarblog/<pk>", views.eliminar_blogs, name="Borrarblog"),
    path("editBlog/<pk>", views.modificar_blogs, name="Editarblog" ),
    path("especificBlog/<pk>", views.blog_especifico, name="Blogespecifico" ),
    path("editProfile", views.editar_perfil, name="EditarPerfil"),
    path("profile", views.perfil_usuario, name="Perfil"),
    path("about", views.about, name="About")
    
    

    
]