from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'Index.html')


def catalogo(request):
    return render(request, 'catalogo.html')


def contacto(request):
    return render(request, 'Contacto.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def producto(request):
    return render(request, 'producto.html')


def base(request):
    return render(request, 'base.html')


def carrito(request):
    return render(request, 'Carrito.html')


def prueba_A(request):
    return render(request, 'prueba-A.html')


def prueba_S(request):
    return render(request, 'prueba-S.html')


def pruebas(request):
    return render(request, 'pruebas.html')
