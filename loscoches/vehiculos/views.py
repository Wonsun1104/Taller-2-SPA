from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
