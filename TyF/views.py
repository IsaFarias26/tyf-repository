from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoJuegos, JuegosDeMesa
from django.contrib.auth.decorators import login_required


def menu(request):
    request.session["usuario"] = "TheShai"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'Index.html')


@login_required
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


def crud(request):
    productos = []
    productos.extend(VideoJuegos.objects.all())
    productos.extend(JuegosDeMesa.objects.all())

    context = {
        'productos': productos
    }
    return render(request, 'crud.html', context)


def crear_producto(request):
    if request.method == 'POST':
        form = VideoJuegosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = VideoJuegosForm()

    context = {
        'form': form
    }
    return render(request, 'crear_producto.html', context)


def editar_producto(request, pk):
    producto = get_object_or_404(VideoJuegos, pk=pk)
    if request.method == 'POST':
        form = VideoJuegosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = VideoJuegosForm(instance=producto)

    context = {
        'form': form,
        'producto': producto
    }
    return render(request, 'editar_producto.html', context)


def eliminar_producto(request, pk):
    producto = get_object_or_404(VideoJuegos, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('crud')

    context = {
        'producto': producto
    }
    return render(request, 'eliminar_producto.html', context)
