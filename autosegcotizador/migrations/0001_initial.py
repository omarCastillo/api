# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_Asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('precio_asistencia', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CosotoAdministracion',
            fields=[
                ('id_CosotoAdministracion', models.AutoField(primary_key=True, serialize=False)),
                ('precio_costo_administracion', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CosotoComercializacion',
            fields=[
                ('id_CosotoComercializacion', models.AutoField(primary_key=True, serialize=False)),
                ('precio_costo_comercial', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DaniosMateriales',
            fields=[
                ('id_DaniosMateriales', models.AutoField(primary_key=True, serialize=False)),
                ('precio_danios_materiales', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleModelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_clave_marca', models.AutoField(primary_key=True, serialize=False)),
                ('clave_marca', models.IntegerField()),
                ('marca', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MargenUtilidad',
            fields=[
                ('id_MargenUtilidad', models.AutoField(primary_key=True, serialize=False)),
                ('precio_margen_utilidad', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_clave_modelo', models.AutoField(primary_key=True, serialize=False)),
                ('clave_modelo', models.IntegerField()),
                ('clave_marca', models.IntegerField(null=True)),
                ('modelo', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rc',
            fields=[
                ('id_Rc', models.AutoField(primary_key=True, serialize=False)),
                ('precio_rc', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Robo',
            fields=[
                ('id_Robo', models.AutoField(primary_key=True, serialize=False)),
                ('precio_robo', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoCobro',
            fields=[
                ('id_TipoCobro', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cobro', models.BooleanField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ValuacionAutoseg',
            fields=[
                ('id_ValuacionAutoseg', models.AutoField(primary_key=True, serialize=False)),
                ('precio_valuacion_autoseg', models.IntegerField()),
                ('vigencia', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id_clave_version', models.AutoField(primary_key=True, serialize=False)),
                ('clave_version', models.TextField()),
                ('clave_modelo', models.IntegerField(null=True)),
                ('anio', models.IntegerField()),
                ('puertas', models.TextField()),
                ('version', models.TextField()),
                ('version2', models.TextField(null=True)),
                ('linea_nueva', models.TextField(null=True)),
                ('linea_nueva2', models.TextField(null=True)),
                ('valor_ebc', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='detallemodelo',
            name='marca',
            field=models.ManyToManyField(blank=True, to='autosegcotizador.Marca'),
        ),
        migrations.AddField(
            model_name='detallemodelo',
            name='modelo',
            field=models.ManyToManyField(blank=True, to='autosegcotizador.Modelo'),
        ),
    ]
