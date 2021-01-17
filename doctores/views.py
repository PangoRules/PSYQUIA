from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from doctores.models import Paciente, Beck
from . import forms
import numpy as np
import pandas as pd
import datetime
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
	#paciente= Paciente.objects.values().filter(id=2)
	beck= Beck.objects.values().filter(paciente_id=2)

	testbeck = Beck.objects.filter()
	form = forms.RegistrarTestBeckForm()
	#Luego filtrar por el id doctor despues del login
	current_user = request.user
	pacientes = Paciente.objects.values('id','name').filter(doctor_id=current_user.id)
	if request.method == 'POST':
		#model1 = load_model('keras_models/suicide_ac100_loss2.h5')
		#model2 = load_model('keras_models/suicide_ac100_loss2.h5')
		#model3 = load_model('keras_models/suicide_ac100_loss2.h5')

		dataset = pd.read_csv('keras_models/DATASET_SUICIDIO.csv')
		dataset = dataset.drop(['TESTIGO'],axis=1)
		x = dataset.iloc[:,0:61].values

		edad= [datetime.datetime.now().year-paciente[0]['birth_date'].year]
		sexo=[0,0]
		sexo[paciente[0]['sex']]=1
		estudios=[0,0,0,0,0]
		estudios[paciente[0]['study']]=1
		trabajo=[0,0,0,0,0,0,0]
		trabajo[paciente[0]['job']]=1
		civil=[0,0,0,0,0,0]
		civil[paciente[0]['civil_state']]=1
		religion=[0,0,0,0,0,0,0]
		religion[paciente[0]['religion']]=1
		socieconomico=[0]
		socieconomico[0]=paciente[0]['economical_situation']

		sociodemograficos= edad+sexo+estudios+trabajo+civil+religion+socieconomico
		print(sociodemograficos)
		#inputs =  pd.DataFrame(prueba)
		#a= np.array(inputs.replace(np.nan, 0).T)
		#print(a)
		#new = stats.zscore(np.append(a,x,axis=0),axis=0)
		#dato=pd.DataFrame(new[0]).T
		#ynew = np.round(model.predict(dato))
		#print(ynew)
		form = forms.RegistrarTestBeckForm(request.POST)
		if form.is_valid():
			nuevo_test = form.save(commit=False)
			paciente = Paciente.objects.get(id=request.POST['paciente_id'])
			nuevo_test.paciente = paciente
			form.save()
			return JsonResponse({'respuesta':True})
		else:
			return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})
	context = {'form':form,'paciente':paciente}
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