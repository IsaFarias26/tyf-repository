from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('producto/', views.producto, name='producto'),
    path('pruebas/', views.pruebas, name='pruebas'),
    path('crud/', views.crud, name='crud'),
]
