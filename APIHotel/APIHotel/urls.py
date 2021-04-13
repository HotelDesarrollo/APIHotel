from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/Alojamientos/', include('apps.alojamientos.urls')),
    path('API/Habitaciones/', include('apps.habitaciones.urls')),
    path('API/Usuarios/', include('apps.usuarios.urls')),
]
