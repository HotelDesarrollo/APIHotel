from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Habitacion
from .serializers import habitacionSerializer


class Class_query():
    def get_queryset(self):
        return Habitacion.objects.all()


class listado_habitacion(APIView, Class_query):

    def get(self, request):
        try:
            habitaciones = Habitacion.objects.filter(eliminado="NO").order_by('id')
            serializer = habitacionSerializer(habitaciones, many=True)
            return Response(dict(habitacion=serializer.data))
        except:
            return Response(dict(habitacion=[], detail="not found"))
    
    def post(self, request):
        habitacion = request.data.get('habitacion')
        print(habitacion)
        serializer = habitacionSerializer(data=habitacion)
        if serializer.is_valid(raise_exception=True):
            habitacion_saved = serializer.save()
        return Response(dict(success=f"Habitacion: '{habitacion_saved.nombre}' creada satisfactoriamente".format()))


class detalle_habitacion(APIView, Class_query):
    def get(self, request, pk):
        try:
            habitaciones = Habitacion.objects.get(id=pk)
            serializer = habitacionSerializer(habitaciones)
            return Response(dict(habitaciones=serializer.data))
        except:
            return Response(dict(habitaciones=[], detail="not found"))

    def put(self, request, pk):
        saved_habitaciones = get_object_or_404(Habitacion.objects.all(), id=pk)
        habitaciones = request.data.get('habitaciones')
        print('llego la habitacion: ', habitaciones)
        serializer = habitacionSerializer(
            instance=saved_habitaciones, data=habitaciones, partial=True)
        if serializer.is_valid(raise_exception=True):
            habitacion_saved = serializer.save()
        return Response(dict(success=f'Habitacion [{habitacion_saved.nombre}] actualizada correctamente'))

    def delete(self, request, pk):
        habitaciones = get_object_or_404(Habitacion.objects.all(), id=pk)
        habitaciones.eliminado = 'SI'
        habitacion_saved = habitaciones.save()
        return Response(dict(message=f"Habitacion with id `{pk}` fue eliminada."), status=204)
