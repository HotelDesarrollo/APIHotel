from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Usuarios, Group
from .serializers import usuariosSerializer, gruposSerializer, usuariosgruposSerializer


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
        usuario = request.data.get('usuarios')
        grupo = usuario.pop('tipo_usuario')
        print(grupo)
        serializer = usuariosSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            usuario_saved = serializer.save()
        usuario_saved.groups.add(grupo)
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
        # Listo los grupos con sus permisos asignados
        grupos = Group.objects.all().order_by('id')
        serializer = gruposSerializer(grupos, many=True)
        return Response(dict(grupos_con_permisos=serializer.data, detail="not found"))

class listado_UsuariosPorGrupos(APIView, Class_query):
    def get(self, request):
        # grupo_permisos  = Usuarios.get_group_permissions()
        # grupo_permisos = Usuarios.get_all_permissions()
        # grupo_permisos = Usuarios.objects.filter().first().groups.first().permissions.all()
        # grupo_permisos = Permission.objects.all().order_by('id') # Obtengo todos los permisos
        # grupo_permisos = Usuarios.get_group_permissions()
        # print('grupos:', self.request.Usuarios.groups.all())
        """
            get_group_permissions(): devuelve una lista con los permisos que tiene un usuario, 
            obtenidos a través del grupo o grupos a las que pertenezca.

            <--- Ejemplo --->
            https://python.hotexamples.com/examples/django.contrib.auth.backends/ModelBackend/get_group_permissions/python-modelbackend-get_group_permissions-method-examples.html
        """
        # ----------------------------------------------------------------
        # Obtengo todos los permisos que posee el usuario actual, mediante dos consultas
        # separadas, una sobre grupos y otra sobre permisos y los resultados se guardan en group_ids
        # ----------------------------------------------------------------
        # group_ids = Group.objects.all().values_list('id', flat=True)
        # group_ids = Permission.objects.filter(group__id__in=group_ids)

        # grupo_permisos captura los resultados de group_ids y despues se muestran
        # grupo_permisos = group_ids
        # ----------------------------------------------------------------

        # muestro los usuarios segun su grupo, pero falta agregar el campo id 
        # del grupo en la respuesta y mostrar los usuarios de todos los
        # grupos existentes, ya que solo muestro los usuarios de un grupo
        grupo_permisos = Usuarios.objects.filter(groups__name='prueba')
        serializer = usuariosSerializer(grupo_permisos, many=True)
        print(grupo_permisos)
        return Response(dict(usuarios_segun_grupo=serializer.data, detail="not found"))
        
"""
Para obtener todos los grupos de un usuario, puede hacer esto:
    user.groups.all()
para obtener todos los usuarios de un grupo:
    group.user_set.all()
"""