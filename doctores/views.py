from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from doctores.models import Paciente
from . import forms
import numpy as np
import pandas as pd
from scipy import stats
from keras.models import load_model
from account.decorators import not_authenticated

# Create your views here.

@not_authenticated
def docDashboard(request):
	#Cambiar para que filtre por idDoctor
	current_user = request.user
	pacientes = Paciente.objects.all().filter(doctor_id=current_user.id)
	cabeceras = ['Nombre', 'Edad', 'Último Grado de Estudios', 'Ocupación', 'Nivel Económico', 'Correo Electrónico']
	context={'cabeceras':cabeceras,'pacientes':pacientes}
	return render(request, "doctor/dashboard.html",context)

def docTest(request):
	return render(request, "doctor/test.html")

@not_authenticated
def docBeck(request):
	form = forms.RegistrarTestBeckForm()
	#Luego filtrar por el id doctor despues del login
	current_user = request.user
	pacientes = Paciente.objects.values('id','name').filter(doctor_id=current_user.id)
	if request.method == 'POST':
		model = load_model('keras_models/suicide_ac100_loss2.h5')
		dataset = pd.read_csv('keras_models/DATASET_SUICIDIO.csv')
		dataset = dataset.drop(['TESTIGO'],axis=1)
		x = dataset.iloc[:,0:61].values
		prueba = [
        23,#EDAD
        1,#HOMBRE
        0,#MUJER
        0,#SIN ESTUDIOS
        0,#SECUNDARIA
        0,#MEDIA SUPERIOR
        1,#SUPERIOR
        0,#POSGRADO
        0,#ESTUDIANTE
        0,#AMA DE CASA
        0,#EMPLEADO
        0,#NADA
        0,#OFICIO
        0,#EMPRENDEDOR
        1,#PROFESION
        1,#SOLTERO
        0,#CASADO
        0,#VIUDO
        0,#DIVORCIADO
        0,#UNION LIBRE
        0,#SEPARADO
        1,#CATOLICO
        0,#CRISTIANO
        0,#ATEO
        0,#ADVENTISTA
        0,#OTRA
        0,#NINGUNA
        2,#SOCIECNONOMICO
        1,#1
        2,#2
        1,#3
        2,#4
        2,#5
        1,#6
        2,#7
        1,#8
        1,#10
        1,#11
        1,#12
        1,#13
        1,#14
        1,#15
        1,#16A
        0,#16B
        2,#17
        0,#18A
        1,#18B
        2,#19
        1,#20
        1,#21
        0,#VIVIR SOLO
        1,#CONFLICTO FAMILIAR
        0,#MUERTE FAMILIAR
        0,#PRESION REDES
        0,#DIAS FESTIVOS
        0,#DIVORCIO PADRES
        0,#PERDIDA TRABAJO
        1,#CONFLICTO LABORAL
        0,#SEPARACIÓN
        1,#ABUSO SEXUAL
        0]#AMOROSO
		
		inputs =  pd.DataFrame(prueba)
		a= np.array(inputs.replace(np.nan, 0).T)
		print(a)
		new = stats.zscore(np.append(a,x,axis=0),axis=0)
		dato=pd.DataFrame(new[0]).T
		ynew = np.round(model.predict(dato))
		print(ynew)
		form = forms.RegistrarTestBeckForm(request.POST)
		if form.is_valid():
			nuevo_test = form.save(commit=False)
			paciente = Paciente.objects.get(id=request.POST['paciente_id'])
			nuevo_test.paciente = paciente
			form.save()
			return JsonResponse({'respuesta':True})
		else:
			return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})
	context = {'form':form,'paciente':pacientes}
	return render(request, "doctor/beck.html",context)

@not_authenticated
def docRegPaciente(request):
	form = forms.RegistrarPacienteForm()
	if request.method == 'POST':
		form = forms.RegistrarPacienteForm(request.POST)
		if form.is_valid():
			nuevo_paciente = form.save(commit=False)
			nuevo_paciente.doctor = request.user
			form.save()
			return JsonResponse({'respuesta':True})
		else:
			return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})
	context = {'form':form}
	return render(request, "doctor/registrarpaciente.html",context)

@not_authenticated
def docCasoDistimico(request):
	return render(request, "doctor/casodistimico.html")

@not_authenticated
def docCasoDepresivo(request):
	return render(request, "doctor/casodepresivo.html")