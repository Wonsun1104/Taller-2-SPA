from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()
    referencia = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now=True)
    valor_comercial = models.BigIntegerField()

    def __str__(self):
        return f'{self.marca} {self.referencia} ({self.modelo})'
