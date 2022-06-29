from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto 


class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente 
        fields = ['idCliente', 'nombreCliente', 'correo', 'direccion']
        labels ={
            'idCliente' : 'IdCliente',
            'nombreCliente' : 'NombreCliente',
            'correo' : 'Correo',
            'direccion' : 'Direccion',
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
            'Correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el correo del cliente', 
                    'id': 'correo'
                }
            ),
             'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el direccion del cliente', 
                    'id': 'direccion'
                }
            ),
        





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

       
        
        
        
        
 