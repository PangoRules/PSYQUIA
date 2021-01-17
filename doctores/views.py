from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from doctores.models import Paciente, Beck
from . import forms
import numpy as np
import pandas as pd
from scipy import stats
from keras.models import load_model
from datetime import datetime

# Create your views here.

def docDashboard(request):
	return render(request, "doctor/dashboard.html")

def docTest(request):
	return render(request, "doctor/test.html")

def docBeck(request):
	paciente= Paciente.objects.values().filter(id=2)
	beck= Beck.objects.values().filter(paciente_id=2)

	testbeck = Beck.objects.filter()
	form = forms.RegistrarTestBeckForm()
	#Luego filtrar por el id doctor despues del login
	pacientes = Paciente.objects.values('id','name')
	if request.method == 'POST':
		model = load_model('keras_models/suicide_ac100_loss2.h5')
		dataset = pd.read_csv('keras_models/DATASET_SUICIDIO.csv')
		dataset = dataset.drop(['TESTIGO'],axis=1)
		x = dataset.iloc[:,0:61].values
		edad= [datetime.now().year-paciente[0]['birth_date'].year]
		if paciente[0]['sex']=='1':
			sexo=[1,0]
		else:
			sexo=[0,1]
		print(sexo)

		#inputs =  pd.DataFrame(prueba)
		#a= np.array(inputs.replace(np.nan, 0).T)
		#print(a)
		#new = stats.zscore(np.append(a,x,axis=0),axis=0)
		#dato=pd.DataFrame(new[0]).T
		#ynew = np.round(model.predict(dato))
		#print(ynew)
		
	context = {'form':form,'paciente':pacientes}
	return render(request, "doctor/beck.html",context)

def docRegPaciente(request):
	form = forms.RegistrarPacienteForm()
	if request.method == 'POST':
		form = forms.RegistrarPacienteForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'respuesta':True})
		else:
			return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})
	context = {'form':form}
	return render(request, "doctor/registrarpaciente.html",context)

def docCasoDistimico(request):
	return render(request, "doctor/casodistimico.html")

def docCasoDepresivo(request):
	return render(request, "doctor/casodepresivo.html")