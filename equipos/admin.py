from django.contrib import admin
from equipos.models import Jugador, JugadorAdmin, Equipo, EquipoAdmin

#Registramos nuestras clases principales.
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equipo, EquipoAdmin)
