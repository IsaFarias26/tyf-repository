from django.contrib import admin
from django.urls import path, include
from TyF import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('admin/', admin.site.urls),
    path('TyF/', include('TyF.urls')),
    path('account/', include('django.contrib.auth.urls')),
]
