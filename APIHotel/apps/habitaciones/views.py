from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.usuarios.serializers import UserSerializer
from rest_framework import viewsets


def index(request):
    return HttpResponse("<h1> Hola, bienvenido a la aplicacion de usuarios </h1>")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .models import Usuarios
# from .serializers import UsuarioSerializer


# # Create your views here.


# class Class_query():
#     def get_queryset(self):
#         return Usuarios.objects.filter(eliminado="NO").order_by('id')


# class listado_usuarioView(APIView, Class_query):
#     def get(self, request, pk):
#         try:
#             usuario = Usuarios.objects.get(id=pk)
#             serializer = UsuarioSerializer(usuario)
#             return Response(dict(user=serializer.data))
#         except:
#             return Response(dict(user=[], detail="not found"))

#     def put(self, request, pk):
#         saved_usuario = get_object_or_404(
#             Usuarios.objects.all(), id=pk)
#         usuario = request.data.get('usuario')
#         serializer = UsuarioSerializer(
#             instance=saved_usuario, data=usuario, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             usuario_saved = serializer.save()
#         return Response(dict(success=f"Usuarios '{usuario_saved.username}' updated successfully"))

#     def delete(self, request, pk):
#         usuario = get_object_or_404(Usuarios.objects.all(), id=pk)
#         usuario.eliminado = 'SI'
#         return Response(dict(message=f"Usuario with id `{pk}` has been deleted."), status=204)


# class detalle_usuario(APIView, Class_query):
#     def get(self, request):
#         try:
#             usuario = Usuarios.objects.all()
#             serializer = UsuarioSerializer(usuario, many=True)
#             return Response(dict(user=serializer.data))
#         except:
#             return Response(dict(user=[], detail="not found"))

#     def post(self, request):
#         usuario = request.data.get('usuario')
#         print(usuario)
#         serializer = UsuarioSerializer(data=usuario)
#         if serializer.is_valid(raise_exception=True):
#             usuario_saved = serializer.save()
#         return Response(dict(success=f"Usuarios: '{usuario_saved.username}' creado satisfactoriamente".format()))
