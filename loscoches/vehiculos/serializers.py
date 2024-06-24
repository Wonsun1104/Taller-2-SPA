from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id','marca','modelo','referencia','fecha_creacion','valor_comercial']
