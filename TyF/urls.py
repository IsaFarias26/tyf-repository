from django.urls import path, include
from TyF.views import index


urlpatterns = [
    path('inicio/', index),
]
