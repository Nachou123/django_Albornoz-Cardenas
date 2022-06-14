from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto 


class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente 
        fields = ['idCliente', 'nombreCliente', 'apellido', 'comuna']
        labels ={
            'idCliente' : 'IdCliente',
            'nombreCliente' : 'NombreCliente',
            'apellido' : 'Apellido',
            'comuna' : 'Comuna',
        }

        widgets={
            'idCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del cliente', 
                    'id': 'idCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombreCliente'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido del cliente', 
                    'id': 'apellido'
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la comuna del cliente', 
                    'id': 'comuna'
                }
            )  
        





        }

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto']
        labels={'idProducto' : 'IdProducto',
                'nombreProducto' : 'NombreProducto',
        }


        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del producto', 
                    'id': 'idProducto'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del producto', 
                    'id': 'nombreProducto'
                }
            ) 
         }

       
        
        
        
        
 