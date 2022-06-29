from django.shortcuts import render, redirect
from .models import Cliente
from .models import Producto
from .forms import ProductoForm, ClienteForm



# Create your views here.

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def nuestros_productos(request):
    return render(request, 'nuestros_productos.html')

def formularios(request):
    return render(request, 'formularios.html')

def monedas(request):
    return render(request, 'monedas.html')



#mostrar la informacion de las clases
def mostrar_cliente(request):
    clientes = Cliente.objects.all()

    datos= {
        'clientes' : clientes
    }
    return render(request, 'cliente.html', datos)



def mostrar_producto(request):
    productos = Producto.objects.all()

    datoss= {
        'productos' : productos
        }
    return render(request, 'producto.html', datoss)



def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid:
            producto_form.save()
            return redirect ('producto')
    else:
        producto_form = ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_prod(request, id):
    producto = Producto.objects.get(idProducto=id)
    datoss={
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario_prod=ProductoForm(data=request.POST, instance=producto)
        if formulario_prod.is_valid:
            formulario_prod.save()
            return redirect('producto')
    return render(request, 'form_mod_prod.html', datoss)


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('producto')





def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid:
            cliente_form.save()
            return redirect ('cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})


def form_mod_cli(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    datos={
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario_cli=ClienteForm(data=request.POST, instance=cliente)
        if formulario_cli.is_valid:
            formulario_cli.save()
            return redirect('cliente')
    return render(request, 'form_mod_cli.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    cliente.delete()
    return redirect('cliente')



