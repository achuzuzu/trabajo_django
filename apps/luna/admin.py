from django.contrib import admin
from .models import Area, Espacio, Entrenador, Actividad, Evento, Socio

admin.site.register(Entrenador)
admin.site.register(Actividad)
admin.site.register(Area)
admin.site.register(Espacio)
admin.site.register(Socio)
admin.site.register(Evento)


# Register your models here.
