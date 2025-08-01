# Generated by Django 5.2.3 on 2025-06-23 21:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=40, unique=True)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_Actividad', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.area')),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_area', models.CharField(max_length=100)),
                ('propietario', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.area')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('actividades', models.ManyToManyField(blank=True, related_name='eventos', to='luna.actividad')),
                ('espacio_fisico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.espacio')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('actividades', models.ManyToManyField(blank=True, related_name='socios', to='luna.actividad')),
            ],
        ),
    ]
