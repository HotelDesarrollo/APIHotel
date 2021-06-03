from django.urls import path
from .views import listado_usuario, detalle_usuario

app_name = "usuarios"
urlpatterns = [
    path('', listado_usuario.as_view()),
    path('<int:pk>', detalle_usuario.as_view()),
]
