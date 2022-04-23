from django.urls import path
from App import views


urlpatterns = [
    
    path("", views.random_blog, name = "inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("createBlog/", views.Crear_Blog, name="Crear"),
    path("messages", views.mensaje, name = "mensajeria"),
    path("pages", views.leerblogs, name="leerblogs"),
    path("eliminarblog/<pk>", views.eliminarblogs, name="Borrarblog"),
    path("editBlog/<pk>", views.modificarBlogs, name="Editarblog" ),
    path("especificBlog/<pk>", views.blogEspecifico, name="Blogespecifico" ),
    path("editProfile", views.editarPerfil, name="EditarPerfil"),
    path("profile", views.PerfilUsuario, name="Perfil"),
    path("about", views.About, name="About")
    
    

    
]