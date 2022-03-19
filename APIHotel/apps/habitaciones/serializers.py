from rest_framework import serializers
from .models import Habitacion
# ejemplo
# https://medium.com/@rudmanmrrod/django-rest-framework-uso-del-depth-en-serializer-a500969779e9
# https://stackoverflow.com/questions/58644572/drf-adding-depth-1-to-model-serializer-no-longer-allows-me-to-post
# https://stackoverflow.com/questions/15883678/django-rest-framework-different-depth-for-post-put/26741062

class habitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = (  'id',
                    'nombre',
                    'descripcion',
                    'precio',
                    'numero_personas',
                    'activo',
                    'eliminado',
                    'nombre_alojamiento',
                )
        depth = 1

class habitacionSerializerPOST(serializers.ModelSerializer):

    class Meta:
        model = Habitacion
        fields = (  'id',
                    'nombre',
                    'descripcion',
                    'precio',
                    'numero_personas',
                    'activo',
                    'eliminado',
                    'nombre_alojamiento',
                    'nombre_alojamiento_id',
                )
    def create(self, validated_data):
        return Habitacion.objects.create(**validated_data)

