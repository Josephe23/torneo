from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.equipo_listar, name ='equipo_listar'),
    url(r'^equipo/nuevo/$', views.equipo_nuevo, name='equipo_nuevo'),
    url(r'^equipo/(?P<pk>[0-9]+)/$', views.equipo_detalle, name='equipo_detalle'),
    url(r'^equipo/(?P<pk>[0-9]+)/editar/$', views.equipo_editar, name='equipo_editar'),
    url(r'^equipo/(?P<pk>\d+)/remover/$', views.equipo_remover, name='equipo_remover'),
    url(r'^jugador/nuevo/$', views.jugador_nuevo, name= 'jugador_nuevo'),
    url(r'^jugador/lista/$', views.jugador_listar, name = 'jugador_listar'),
    url(r'^jugador/(?P<pk>[0-9]+)/$', views.jugador_detalle, name='jugador_detalle'),
    url(r'^jugador/(?P<pk>[0-9]+)/editar/$', views.jugador_editar, name='jugador_editar'),
    url(r'^jugador/(?P<pk>\d+)/remover/$', views.jugador_remover, name='jugador_remover'),
    ]
