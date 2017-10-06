# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
  id_clave_marca = models.AutoField(primary_key=True)
  clave_marca = models.IntegerField()
  marca = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  def __unicode(self):
        return 'Marca: ' + self.marca

class Modelo(models.Model):
  id_clave_modelo = models.AutoField(primary_key=True)
  clave_modelo = models.IntegerField()
  clave_marca = models.IntegerField(null=True)
  modelo = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  def __unicode(self):
        return 'Modelos: ' + self.modelo

class Version(models.Model):
  id_clave_version = models.AutoField(primary_key=True)  
  clave_version = models.TextField()
  clave_modelo = models.IntegerField(null=True)
  anio = models.IntegerField()
  puertas = models.TextField()
  version = models.TextField()
  version2 = models.TextField(null=True)
  linea_nueva = models.TextField(null=True)
  linea_nueva2 = models.TextField(null=True)
  valor_ebc = models.IntegerField(default=0)
  created_date = models.DateTimeField(default=timezone.now, null=True)
  def __unicode(self):
        return 'Version: ' + self.version

class DetalleModelo(models.Model):
  id = models.AutoField(primary_key=True)
  modelo = models.ManyToManyField(Modelo, blank=True)
  marca = models.ManyToManyField(Marca, blank=True)

class Asistencia(models.Model):
  id_Asistencia = models.AutoField(primary_key=True)
  precio_asistencia = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Asistencia'

class Robo(models.Model):
  id_Robo = models.AutoField(primary_key=True)
  precio_robo = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class Rc(models.Model):
  id_Rc = models.AutoField(primary_key=True)
  precio_rc = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class CosotoComercializacion(models.Model):
  id_CosotoComercializacion = models.AutoField(primary_key=True)
  precio_costo_comercial = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class CosotoAdministracion(models.Model):
  id_CosotoAdministracion = models.AutoField(primary_key=True)
  precio_costo_administracion = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class MargenUtilidad(models.Model):
  id_MargenUtilidad = models.AutoField(primary_key=True)
  precio_margen_utilidad = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class ValuacionAutoseg(models.Model):
  id_ValuacionAutoseg = models.AutoField(primary_key=True)
  precio_valuacion_autoseg = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class DaniosMateriales(models.Model):
  id_DaniosMateriales = models.AutoField(primary_key=True)
  precio_danios_materiales = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'

class TipoCobro(models.Model):
  id_TipoCobro = models.AutoField(primary_key=True)
  tipo_cobro = models.BooleanField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Tipo de cobro'

class Horario(models.Model):
  id_horario = models.AutoField(primary_key=True)
  clave_horario = models.IntegerField()
  horario = models.TimeField(auto_now=False, auto_now_add=False)
  def __unicode(self):
        return 'Horario'

class Sucursal(models.Model):
  id_sucursal = models.AutoField(primary_key=True)
  clave_horario = models.IntegerField()
  cp_sucursal = models.TextField()
  calle_sucursal = models.TextField()
  estado_sucursal = models.TextField()
  colonia_sucursal = models.TextField()

class DerechoMembresia(models.Model):
  id_derechoMembresia = models.AutoField(primary_key=True)
  precio_derecho_membresia = models.IntegerField()
  vigencia = models.DateField()
  status = models.BooleanField()
  def __unicode(self):
        return 'Precio'
