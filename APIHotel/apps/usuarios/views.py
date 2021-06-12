from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Usuarios, Group
from .serializers import gruposSerializer, usuariosSerializer


class Class_query():
    def get_queryset(self):
        return Usuarios.objects.all()

class listado_usuario(APIView, Class_query):
    def get(self, request):
        try:
            usuarios = Usuarios.objects.filter(eliminado="NO").order_by('id')
            serializer = usuariosSerializer(usuarios, many=True)
            return Response(dict(usuario=serializer.data))
        except:
            return Response(dict(usuario=[], detail="not found"))

    def post(self, request):
        usuario = request.data.get('usuario')
        print(usuario)
        serializer = usuariosSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            usuario_saved = serializer.save()
        return Response(dict(success=f"Usuarios: '{usuario_saved.username}' creado satisfactoriamente".format()))


class detalle_usuario(APIView, Class_query):
    def get(self, request, pk):
        try:
            usuario = Usuarios.objects.get(id=pk)
            serializer = usuariosSerializer(usuario, many=True)
            return Response(dict(usuario=serializer.data))
        except:
            return Response(dict(usuario=[], detail="not found"))

    def put(self, request, pk):
        saved_usuario = get_object_or_404(
            Usuarios.objects.all(), id=pk)
        usuario = request.data.get('usuario')
        print('llego el usuario: ', usuario)
        serializer = usuariosSerializer(
            instance=saved_usuario, data=usuario, partial=True)
        if serializer.is_valid(raise_exception=True):
            usuario_saved = serializer.save()
        return Response(dict(success=f"Usuarios '{usuario_saved.username}' actualizado correctamente"))

        def delete(self, request, pk):
            usuario = get_object_or_404(Usuarios.objects.all(), id=pk)
            usuario.eliminado = 'SI'
            usuario_saved = usuario.save()
            return Response(dict(message=f"Usuario con id `{pk}` fue eliminado."), status=204)


class listado_grupos(APIView, Class_query):
    def get(self, request):
        grupos = Group.objects.all().order_by('id')
        serializer = gruposSerializer(grupos, many=True)
        print('sadsa')
        return Response(dict(grupos=serializer.data, detail="not found"))
