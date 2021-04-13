from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.index, name='index')
    path('', include(router.urls))
]










# from django.urls import path
# from .views import listado_usuarioView, detalle_usuario

# app_name = "usuarios"
# urlpatterns = [
#     path('', detalle_usuario.as_view()),
#     path('<int:pk>', listado_usuarioView.as_view())
# ]
