from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ProductoBase(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=10)
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


class Meta:
    abstract = True
    def __str__(self): return self.titulo


class VideoJuegos(ProductoBase):
    plataforma = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)


class JuegosDeMesa(ProductoBase):
    numero_jugadores = models.CharField(max_length=100)
    edad_recomendada = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self): return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre


class ProductoCategoria(models.Model):
    producto_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    producto_object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('producto_content_type', 'producto_object_id')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class ProductoEtiqueta(models.Model):
    producto_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    producto_object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('producto_content_type', 'producto_object_id')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
