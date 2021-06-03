from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuarios(AbstractUser):
    objects: models.Manager()
    direccion = models.CharField(max_length=250)
    tipo_usuario = models.CharField(max_length=15)
    estado = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    eliminado = models.CharField(max_length=2, default='NO')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'

