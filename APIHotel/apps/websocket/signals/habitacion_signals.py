import json
from unittest import result
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from apps.websocket.signals import types_dict_convert

from apps.habitaciones.models import Habitacion

@receiver(post_save, sender=Habitacion)
def announce_new_habitacion(sender, instance, created, **kwargs):
    if created:
        print('se llamo al create')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="Habitacion",
                            event="c", data=types_dict_convert)
        )


@receiver(post_save, sender=Habitacion)
def announce_update_habitacion(sender, instance, created, **kwargs):
    if not created:
        print('se llamo al update')
        dict_obj = model_to_dict(instance)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cambios", dict(type="cambios", model="Habitacion",
                            event="u", data=types_dict_convert)
            
            # event="u", data=model_to_dict(instance))
            # buscar como hacer que la instancia de model_to_dict convierta a decimal
        )


@receiver(post_delete, sender=Habitacion)
def announce_del_habitacion(sender, instance, **kwargs):
    print('se llamo al delete')
    dict_obj = model_to_dict(instance)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "cambios", dict(type="cambios", model="Habitacion",
                        event="d", data=model_to_dict(instance))
    )
