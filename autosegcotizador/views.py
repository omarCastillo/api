from django.shortcuts import render

from .models import *

from .serializers import *

from django_filters import rest_framework as filters
import django_filters
from django.contrib.auth.models import User
from django.http.response import HttpResponse

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# API - Views
"""""""""
API endpoint that allows users to be viewed or edited.
"""""""""
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('marca','clave_marca')

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('clave_modelo','modelo','clave_marca')

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('clave_modelo','version','clave_version')

class DaniosViewSet(viewsets.ModelViewSet):
    queryset = DaniosMateriales.objects.all()
    serializer_class = DaniosSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id_DaniosMateriales')

# Variables definidas

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = AsistenciaSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class RoboViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = RoboSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class RcViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = RcSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')   

class CosotoComercializacionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = CosotoComercializacionSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class CosotoAdministracionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = CosotoAdministracionSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class MargenUtilidadViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = MargenUtilidadSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class ValuacionAutosegViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = ValuacionAutosegSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio','vigencia','status')

class DaniosMaterialesViewSet(viewsets.ModelViewSet):
    queryset = DaniosMateriales.objects.all()
    serializer_class = DaniosMaterialesSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio_danios_materiales', 'status')

class TipoCobroViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = TipoCobroSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('tipo_cobro','status')

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = SucursalSerilizer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id_sucursal', 'clave_horario', 'cp_sucursal', 'calle_sucursal', 'estado_sucursal', 'colonia_sucursal')

class DerechoMembresiaViewSet(viewsets.ModelViewSet):
    queryset = DerechoMembresia.objects.all()
    serializer_class = DerechoMembresiaSerilizer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('precio_derecho_membresia', 'status')

@api_view(['GET'])
def suma_variables(request):
    datos_asistencia = Asistencia.objects.get(status=True)
    # serializer = AsistenciaSerializer(pk=6)
    datos_robo = Robo.objects.get(status=True)
    datos_rc = Rc.objects.get(status=True)
    datos_costo_comercializacion = CosotoComercializacion.objects.get(status=True)
    datos_costo_administracion = CosotoAdministracion.objects.get(status=True)
    datos_margen_utilidad = MargenUtilidad.objects.get(status=True)
    datos_valuacion_autoseg = ValuacionAutoseg.objects.get(status=True)
    datos_danios_materiales = DaniosMateriales.objects.get(status=True)

    suma = datos_asistencia.precio_asistencia + datos_robo.precio_robo + datos_rc.precio_rc + datos_costo_comercializacion.precio_costo_comercial + datos_costo_administracion.precio_costo_administracion + datos_margen_utilidad.precio_margen_utilidad + datos_valuacion_autoseg.precio_valuacion_autoseg + datos_danios_materiales.precio_danios_materiales

    # return Response(serializer.data[0]['precio_asistencia'])
    return Response({"result": suma})