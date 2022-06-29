from django.db import models

# Create your models here.

class Cliente (models.Model):
    idCliente = models.CharField(primary_key=True, max_length=9, verbose_name="IdCliente")
    nombreCliente = models.CharField(max_length=50, verbose_name="NombreCliente")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    direccion = models.CharField(max_length=50, verbose_name="Direccion")

    def __str__(self):
        return self.idCliente

class Producto (models.Model):
    idProducto = models.CharField(primary_key=True, max_length=9, verbose_name="IdProducto")
    nombreProducto = models.CharField(max_length=50, verbose_name="NombreProducto")

    def __str__(self):
        return self.idProducto



