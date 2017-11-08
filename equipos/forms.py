from django import forms
from .models import Equipo, Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('nombre', 'liga', 'jugadores')
    def __init__ (self, *args, **kwargs):
        super(EquipoForm, self).__init__(*args, **kwargs)
        self.fields["jugadores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["jugadores"].help_text = "Ingrese los Jugadores que participaron en el Equipo"
        self.fields["jugadores"].queryset = Jugador.objects.all()

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = {'nombre', 'apellido', 'edad'}
