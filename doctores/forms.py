from django import forms
from doctores.models import Beck, Paciente

sexo = (('1', 'Hombre'),('2', 'Mujer'))
estudio = (('1', 'Sin estudios'),('2', 'Secundaria o menor'),('3', 'Media Superior'),('4', 'Superior'),('5', 'Posgrado'))
ocupacion = (('1', 'Sin ocupación'),('2', 'Estudios'),('3', 'Amo(a) de casa'),('4', 'Empleado(a) de empresa'),('5', 'Oficio o técnico'),('6', 'Emprendedor(a)'),('7', 'Profesionista'))
civil = (('1', 'Soltero'),('2', 'Casado'),('3', 'Unión libre'),('4', 'Viudo'),('5', 'Divorciado'),('6', 'Separado'))
religionChoices = (('1', 'Ninguna'),('2', 'Católica'),('3', 'Cristiano'),('4', 'Adventista'),('5', 'Ateo/Agnóstico'),('6', 'Otro'))
situacion = (('0', 'Bajo'),('1', 'Medio-bajo'),('2', 'Mediano'),('3', 'Medio-alto'),('4', 'Alto'))

class RegistrarPacienteForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, required=True,help_text='Requerido. Agregue una dirección de correo válida', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Correo Electronico'}))
    birth_date = forms.CharField(required=True,help_text='Requerido. Agregue una fecha válida', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Fecha de nacimiento'}))
    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=sexo)
    name = forms.CharField(max_length=60, required=True, help_text='Seleccione una opción por favor',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre del paciente'}))
    study = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=estudio)
    job = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=ocupacion)
    civil_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=civil)
    religion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=religionChoices)
    economical_situation = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control',}), choices=situacion)
    class Meta:
        model = Paciente
        fields = ("email","birth_date","sex","name","study","job","civil_state","religion","economical_situation")