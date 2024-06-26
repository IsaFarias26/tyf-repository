from django.contrib import admin
from django.urls import path, include
from TyF import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('TyF/', include('TyF.urls')),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('producto/', views.producto, name='producto'),
    path('pruebas/', views.pruebas, name='pruebas'),
    path('crud/', views.crud, name='crud'),
]
