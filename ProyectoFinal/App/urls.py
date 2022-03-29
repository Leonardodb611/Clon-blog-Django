from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("formulario/", views.usuarioFormulario, name = "Formulario"),
    path("busqueda/", views.busqueda1, name="Busqueda"),
    path("busqueda/usuario", views.busquedaUsuario, name="Busqueda_usuario"),
    path("busqueda/blog", views.busquedaBlog, name="Busqueda_blog"),
    path("busqueda/producto", views.busquedaProducto, name="Busqueda_producto"),
    path("buscar/", views.busqueda),
    path("crear_Blog/", views.Crear_Blog, name="Crear"),
    path("resultado_blog", views.busquedablog),
    path("resultado_ventas", views.busquedaproducto), 
    path("nuevo_Producto", views.crear_Producto, name="Nuevo")
    
]