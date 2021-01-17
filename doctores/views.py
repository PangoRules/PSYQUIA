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
		form = forms.RegistrarTestBeckForm(request.POST)
		if form.is_valid():
			print('entro')
			nuevo_test = form.save(commit=False)
			paciente = Paciente.objects.get(id=request.POST['paciente_id'])
			nuevo_test.paciente = paciente
			form.save()
			model1 = load_model('keras_models/suicide_ac100_loss2.h5')
			model2 = load_model('keras_models/modelTrastornos9_acc93_loss32.h5')
			model3 = load_model('keras_models/modelTipo_acc100_loss63.h5')
			print(paciente.job)
			dataset = pd.read_csv('keras_models/DATASET_SUICIDIO.csv')
			dataset = dataset.drop(['TESTIGO'],axis=1)
			x = dataset.iloc[:,0:61].values
			edad= [datetime.datetime.now().year-paciente.birth_date.year]
			sexo=[0,0]
			sexo[paciente.sex]=1
			estudios=[0,0,0,0,0]
			estudios[paciente.study]=1
			trabajo=[0,0,0,0,0,0,0]
			trabajo[paciente.job]=1
			civil=[0,0,0,0,0,0]
			civil[paciente.civil_state]=1
			religion=[0,0,0,0,0,0]
			religion[paciente.religion]=1
			socieconomico=[0]
			socieconomico[0]=paciente.economical_situation

			sociodemograficos= edad+sexo+estudios+trabajo+civil+religion+socieconomico
			beck= [nuevo_test.tristeza,#0
			nuevo_test.pesimismo,#1
			nuevo_test.fracaso,#2
			nuevo_test.placer,#3
			nuevo_test.culpa,#4
			nuevo_test.castigo,#5
			nuevo_test.disconformidad,#6
			nuevo_test.autocritica,#7
			nuevo_test.llanto,#8
			nuevo_test.agitacion,#9
			nuevo_test.interes,#10
			nuevo_test.indecision,#11
			nuevo_test.desvalorizacion,#12
			nuevo_test.energia,#13
			0,0,#14,15
			nuevo_test.irritabilidad,#16
			0,0,#17,18
			nuevo_test.concentracion,#19
			nuevo_test.fatiga,#20
			nuevo_test.sexo,#21
			int(nuevo_test.vivir_solo == True),#22
			int(nuevo_test.conflicto_familiar == True),#23
			int(nuevo_test.muerte_ser_querido == True),#24
			int(nuevo_test.presion_redes_sociales == True),#25
			int(nuevo_test.dias_festivos == True),#26
			int(nuevo_test.divorcio_padres == True),#27
			int(nuevo_test.perdida_trabajo == True),#28
			int(nuevo_test.conflicto_laboral == True),#29
			int(nuevo_test.separacion_conyugal == True),#30
			int(nuevo_test.abuso_sexual == True),#31
			int(nuevo_test.conflicto_amoroso == True)]#32
			if nuevo_test.sueño[1]=="a":
				beck[14]=int(nuevo_test.apetito[0])
			elif nuevo_test.sueño[1]=="b":
				beck[15]=int(nuevo_test.apetito[0])	
			if nuevo_test.apetito[1]=="a":
				beck[17]=int(nuevo_test.apetito[0])
			elif nuevo_test.apetito[1]=="b":
				beck[18]=int(nuevo_test.apetito[0])
			registro_diagnostico=sociodemograficos+beck
			print(len(registro_diagnostico))
			inputs =  pd.DataFrame(registro_diagnostico)
			a= np.array(inputs.replace(np.nan, 0).T)
			print(a)
			new = stats.zscore(np.append(a,x,axis=0),axis=0)
			dato=pd.DataFrame(new[0]).T
			suicidio_diagnostico = np.round(model1.predict(dato))
			trastorno = np.round(model2.predict(dato))
			print(dato)
			print(dato.iloc[:,28:50].values)
			tipo_trastorno=np.round(model3.predict(dato.iloc[:,28:50].values))
			print("El paciente se va a suicidar?: -","nel" if(suicidio_diagnostico==0) else "si")
			print(trastorno[0][0])
			print(tipo_trastorno)
			print("El paciente tiene depresion?: -","nel" if(trastorno[0][0]==0) else "si")
			print("El paciente tiene distimia?: -","nel" if(trastorno[0][1]==0) else "si")
			
			print("El paciente tiene melancolico?: -","nel" if(tipo_trastorno[0][0]==0) else "si")
			print("El paciente tiene atipico?: -","nel" if(tipo_trastorno[0][1]==0) else "si")
			print("El paciente tiene catatonico?: -","nel" if(tipo_trastorno[0][2]==0) else "si")
			 

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