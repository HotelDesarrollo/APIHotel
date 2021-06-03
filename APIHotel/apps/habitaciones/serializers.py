from rest_framework import serializers
from .models import Habitacion
from ..alojamientos.models import Alojamiento


class habitacionSerializer(serializers.ModelSerializer):
    alojamiento = serializers.ReadOnlyField(source='Alojamiento.nombre.nombre_alojamiento')

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
                    'alojamiento'
                )
