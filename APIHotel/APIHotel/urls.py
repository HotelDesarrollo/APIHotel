from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/Alojamientos/', include('apps.alojamientos.urls')),
    path('API/Habitaciones/', include('apps.habitaciones.urls')),
    path('API/Usuarios/', include('apps.usuarios.urls')),
]

urlpatterns += [
    path('api/auth/', obtain_jwt_token),
    path('api/auth/refresh/', refresh_jwt_token),
    path('api/auth/verify/', verify_jwt_token),
]

