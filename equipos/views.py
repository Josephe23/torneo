from django.shortcuts import render
from django.contrib import messages
from .forms import EquipoForm
from .forms import JugadorForm
from equipos.models import Equipo, Competencia, Jugador
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def equipo_listar(request):
    equipo = Equipo.objects.all()
    return render(request, 'equipos/equipo_listar.html', {'equipo':equipo})

def jugador_listar(request):
    jugador = Jugador.objects.all()
    return render(request, 'equipos/jugador_listar.html', {'jugador':jugador})

@login_required
def equipo_nuevo(request):
    if request.method == "POST":
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            equipo = Equipo.objects.create(nombre=formulario.cleaned_data['nombre'], liga = formulario.cleaned_data['liga'])
            for jugador_id in request.POST.getlist('jugadores'):
                competicion = Competencia(jugador_id=jugador_id, equipo_id = equipo.id)
                competicion.save()
            messages.add_message(request, messages.SUCCESS, 'Equipo guardado Exitosamente')
    else:
        formulario = EquipoForm()
    return render(request, 'equipos/equipo_editar.html', {'formulario': formulario})

@login_required
def jugador_nuevo(request):
    if request.method == "POST":
        formulario = JugadorForm(request.POST)
        if formulario.is_valid():
            jugador = formulario.save(commit=False)
            jugador.save()
            return redirect('jugador_listar')
    else:
        formulario = JugadorForm()
    return render(request, 'equipos/jugador_editar.html', {'formulario': formulario})

@login_required
def jugador_editar(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == "POST":
        formulario = JugadorForm(request.POST, instance=jugador)
        if  formulario.is_valid():
            jugador = formulario.save(commit=False)
            jugador.save()
            return render(request, 'jugador_detalle', pk=jugador.pk)
    else:
        formulario = JugadorForm(instance=jugador)
    return render(request, 'equipos/jugador_editar.html', {'formulario': formulario})

@login_required
def equipo_editar(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        formulario = EquipoForm(request.POST, instance = equipo)
        if formulario.is_valid:
            equipo = formulario.save(commit=False)
            equipo.save()
            return redirect('equipo_detalle', pk=equipo.pk)
    else:
        formulario = EquipoForm(instance=equipo)
    return render(request, 'equipos/equipo_editar.html', {'formulario':formulario})

def equipo_detalle(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipos/equipo_detalle.html', {'equipo': equipo})

def jugador_detalle(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    return render(request, 'equipos/equipo_detalle.html', {'jugador': jugador})

@login_required
def equipo_remover(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    equipo.delete()
    return redirect('equipo_listar')

@login_required
def jugador_remover(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    jugador.delete()
    return redirect('jugador_listar')
