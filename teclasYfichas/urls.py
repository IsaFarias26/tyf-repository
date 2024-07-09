from django.contrib import admin
from django.urls import path, include
from TyF import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('TyF/', include('TyF.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]