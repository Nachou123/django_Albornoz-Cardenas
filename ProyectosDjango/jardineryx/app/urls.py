from django.urls import path
from .views import index, quienes_somos, nuestros_productos, formularios, monedas, mostrar_cliente, mostrar_producto, form_crear_producto, form_crear_cliente, form_mod_prod, form_del_producto,form_mod_cli,form_del_cliente
urlpatterns = [
    path('', index,name="index"),
    path('quienes_somos/', quienes_somos,name="quienes_somos"),
    path('nuestros_productos/', nuestros_productos,name="nuestros_productos"),
    path('formularios/', formularios,name="formularios"),
    path('monedas/', monedas,name="monedas"),
    path('cliente/', mostrar_cliente,name="cliente"),
    path('producto/', mostrar_producto,name="producto"),
    path('form_crear_producto/', form_crear_producto,name="form_crear_producto"),
    path('form_crear_cliente/', form_crear_cliente,name="form_crear_cliente"),
    path('form_mod_prod<id>', form_mod_prod, name="form_mod_prod"),
    path('form_del_producto<id>', form_del_producto, name="form_del_producto"),
    path('form_mod_cli<id>', form_mod_cli, name="form_mod_cli"),
    path('form_del_cliente<id>', form_del_cliente, name="form_del_cliente"),

]