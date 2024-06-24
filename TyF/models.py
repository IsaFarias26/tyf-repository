from django.conf import settings
from django.db import models
from django.utils import timezone


class VideoJuegos(models.Model):
    Autor = models.TextField()
    Titulo = models.CharField(max_length=200)
    Descripción = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class JuegosDeMesa(models.Model):
    Autor = models.TextField()
    Titulo = models.CharField(max_length=200)
    Descripción = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
