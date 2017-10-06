from rest_framework import serializers
from .models import *

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id_clave_marca','clave_marca','marca')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id_clave_modelo','clave_modelo','clave_marca','modelo')

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

class DaniosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaniosMateriales
        fields = '__all__'

class DetalleModeloSerializer (serializers.ModelSerializer):
    modelo = ModeloSerializer(many=True) 
    marca = MarcaSerializer(many=True) 
    class Meta:
        model = DetalleModelo
        fields = '__all__'

# Variables definidas

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class RoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robo
        fields = '__all__'

class RcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rc
        fields = '__all__'

class CosotoComercializacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosotoComercializacion
        fields = '__all__'

class CosotoAdministracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosotoAdministracion
        fields = '__all__'

class MargenUtilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MargenUtilidad
        fields = '__all__'

class ValuacionAutosegSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValuacionAutoseg
        fields = '__all__'

class DaniosMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaniosMateriales
        fields = '__all__'

class TipoCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCobro
        fields = '__all__'

class SucursalSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class DerechoMembresiaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = DerechoMembresia
        fields = '__all__'
   