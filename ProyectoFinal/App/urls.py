from django.urls import path
from App import views


urlpatterns = [
    
    path("", views.random_blog, name = "inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("formulario/", views.usuarioFormulario, name = "Formulario"),
    path("crear_Blog/", views.Crear_Blog, name="Crear"),
    path("mensaje", views.mensaje, name = "mensajeria"),
    path("blogs", views.leerblogs, name="leerblogs"),
    path("eliminarblog/<pk>", views.eliminarblogs, name="Borrarblog"),
    path("editarblog/<pk>", views.modificarBlogs, name="Editarblog" ),
    path("blogespecifico/<pk>", views.blogEspecifico, name="Blogespecifico" ),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil")
    

    
    
    
    
]