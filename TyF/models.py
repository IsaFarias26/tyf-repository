from django.conf import settings
from django.db import models
from django.utils import timezone


class VideoJuegos(models.Model):
    autor = models.TextField()
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class JuegosDeMesa(models.Model):
    autor = models.TextField()
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
