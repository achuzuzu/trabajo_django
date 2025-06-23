from django.db import models
from django.utils import timezone


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=40, unique=True)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=40)

      
    def _str_(self):
        return {self.nombre}



class Area(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.CharField(max_length=100) 
    activo = models.BooleanField(default=True) 
    categoria = models.CharField(max_length=50) 


    def _str_(self):
        return {self.nombre}


class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_area = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return f"{self.nombre} ({self.area.nombre})"
        


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    tipo_Actividad = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    actividades = models.ManyToManyField(Actividad, related_name='eventos', blank=True)
    espacio_fisico = models.ForeignKey(Espacio, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre}"

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    actividades = models.ManyToManyField(Actividad, related_name='socios', blank=True)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"