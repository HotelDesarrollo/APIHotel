from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from apps.usuarios.views import MyTokenObtainPairView

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alojamientos/', include('apps.alojamientos.urls')),
    path('api/habitaciones/', include('apps.habitaciones.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
]

# urlpatterns += [
#     path('api/auth/', obtain_jwt_token),
#     path('api/auth/refresh/', refresh_jwt_token),
#     path('api/auth/verify/', verify_jwt_token),
# ]
urlpatterns += [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
