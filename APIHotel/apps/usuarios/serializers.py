from django.db import models
from rest_framework import serializers
from .models import Usuarios, Group
from django.contrib.auth.models import Group


class usuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields = ('id',
                    'first_name',
                    'last_name',
                    'password',
                    'username',
                    'email',
                    'direccion',
                    'estado',
                    'telefono',
                    'eliminado',
                    'groups'
                )
        depth = 1


class gruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class gruposPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['permissions']


class usuariosSerializerPOST(serializers.ModelSerializer):

    def create(self, validated_data):
        usuario = Usuarios(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        act_usuario = super().update(instance, validated_data)
        act_usuario.set_password(validated_data['password'])
        act_usuario.save()
        return act_usuario

    class Meta:
        model = Usuarios
        fields = (  'id',
                    'first_name',
                    'last_name',
                    'password',
                    'username',
                    'email',
                    'direccion',
                    'estado',
                    'telefono',
                    'eliminado',
                    'groups',
                )


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data.pop('refresh', None)  # remove refresh from the payload
#         data['access'] = str(refresh.access_token)

#         # Add extra responses here
#         data['user'] = self.user.username
#         data['groups'] = self.user.groups
#         return data
