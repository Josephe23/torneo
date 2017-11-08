from django.db import models
from django.contrib import admin

class Jugador(models.Model):
    nombre  =   models.CharField(max_length=30)
    apellido  =   models.CharField(max_length=30)
    edad = models.IntegerField()
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre    = models.CharField(max_length=60)
    liga      = models.CharField(max_length=60)
    jugadores   = models.ManyToManyField(Jugador, through='Competencia')
    def __str__(self):
        return self.nombre

class Competencia(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

class CompetenciaInLine(admin.TabularInline):
    model = Competencia
    extra = 1

class JugadorAdmin(admin.ModelAdmin):
    inlines = (CompetenciaInLine,)

class EquipoAdmin (admin.ModelAdmin):
    inlines = (CompetenciaInLine,)
