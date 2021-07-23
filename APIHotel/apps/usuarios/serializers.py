from django.db import models
from rest_framework import serializers
from .models import Usuarios, Group
from django.contrib.auth.models import Group, Permission

class usuariosSerializer(serializers.ModelSerializer):

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
                )

class gruposSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = '__all__'

class usuariosgruposSerializer(serializers.ModelSerializer):
    class Meta:
        model= Permission
        fields = '__all__'