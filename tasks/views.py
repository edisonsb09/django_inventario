


def home(request):
    return render (request, "inicio.html")

def producto(request):
    # Lógica de la vista del producto
    return render(request, 'producto.html')

def pedidos(request):
    # Lógica de la vista del pedido
    return render(request, 'pedidos.html')

def cliente(request):
    # Lógica de la vista del cliente
    return render(request, 'cliente.html')

def proveedor(request):
    # Lógica de la vista del proveedor
    return render(request, 'proveedor.html')
def menu(request):
    return render (request, "menu.html")

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import BootstrapAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Aquí es donde se realiza el inicio de sesión
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('menu')  # Cambia 'dashboard' por la URL a la que redirigir después de iniciar sesión
            else:
                messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    else:
        form = BootstrapAuthenticationForm()

    return render(request, 'login.html', {'form': form})
