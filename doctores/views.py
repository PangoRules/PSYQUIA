from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from doctores.models import Paciente, Beck, ResultadoDiagnostico
from . import forms
import numpy as np
import pandas as pd
import datetime
from scipy import stats
from keras.models import load_model
from account.decorators import not_authenticated
from django.db.models import Q
from django.core import serializers
import json

# Create your views here.

@not_authenticated
def docGetTestBeck(request):
	id_result_beck = json.loads(request.body)
	id_test_beck = ResultadoDiagnostico.objects.filter(id=id_result_beck).values("beck_id")
	beck = list(Beck.objects.filter(id=id_test_beck[0]['beck_id']).values())
	return JsonResponse({'data':beck})

@not_authenticated
def docGetDatosPaciente(request):
	id_paciente = json.loads(request.body)
	paciente = Paciente.objects.filter(id=id_paciente).values()
	return JsonResponse({'data':list(paciente)})

#Faltan las validaciones
@not_authenticated
def docEditarPaciente(request):
	form = forms.RegistrarPacienteForm(request.POST)
	paciente = Paciente.objects.filter(email=form.data['email']).get()
	paciente.email = form.data['email']
	paciente.birth_date = form.data['birth_date']
	paciente.sex = form.data['sex']
	paciente.name = form.data['name']
	paciente.study = form.data['study']
	paciente.job = form.data['job']
	paciente.civil_state = form.data['civil_state']
	paciente.religion = form.data['religion']
	paciente.economical_situation = form.data['economical_situation']
	paciente.save()
	#print(form.is_valid())
	#if form.is_valid():
	return JsonResponse({'data':True})
	#else:
	#	return JsonResponse({'errores':dict(form.errors.items())})

@not_authenticated
def docDashboard(request):
	#Cambiar para que filtre por idDoctor
	current_user = request.user
	pacientes = Paciente.objects.all().filter(doctor_id=current_user.id)
	resultadosDiagnosticoGeneral = ResultadoDiagnostico.objects.filter(beck__paciente__doctor__id=current_user.id)
	resultadosDiagnosticoDepresivoDistimico = ResultadoDiagnostico.objects.filter(Q(Distimia=True)|Q(Depresion=True),beck__paciente__doctor__id=current_user.id)

	total_casos_depresion_distimia = ResultadoDiagnostico.objects.filter(Q(Distimia=True)|Q(Depresion=True),beck__paciente__doctor__id=current_user.id).count()
	total_casos = ResultadoDiagnostico.objects.filter(beck__paciente__doctor__id=current_user.id).count()
	formEditarPaciente = forms.RegistrarPacienteForm()
	formTestBeck = forms.RegistrarTestBeckForm()

	cabeceras = ['Nombre', 'Edad', 'Último Grado de Estudios', 'Ocupación', 'Nivel Económico', 'Correo Electrónico']
	cabecerasDiagnosticos = ['Nombre', 'Fecha Diagnostico', 'Depresión', 'Distimia']
	cabecerasDiagnosticosDepresivoDistimico = ['Nombre', 'Fecha Diagnostico', 'Depresión', 'Distimia','Tipo de Depresión']
	context={'cabeceras':cabeceras,'pacientes':pacientes, 'total_casos_depresion_distimia':total_casos_depresion_distimia, 
	'total_casos':total_casos, 'cabecerasDiagnosticos':cabecerasDiagnosticos,
	'resultadosDiagnosticoGeneral':resultadosDiagnosticoGeneral,'resultadosDiagnosticoDepresivoDistimico':resultadosDiagnosticoDepresivoDistimico,
	'cabecerasDiagnosticosDepresivoDistimico':cabecerasDiagnosticosDepresivoDistimico, 'formEditarPaciente':formEditarPaciente, 'formTestBeck':formTestBeck,}
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
			tipo_trastorno=[[0,0,0]]

			if trastorno[0][0]==1:
				tipo_trastorno=np.round(model3.predict(dato.iloc[:,28:50].values))
				print('Entro a tipos de depresion')
			


			print("El paciente se va a suicidar?: -","nel" if(suicidio_diagnostico==0) else "si")
			print(trastorno[0][0])
			print(tipo_trastorno)
			print("El paciente tiene depresion?: -","nel" if(trastorno[0][0]==0) else "si")
			print("El paciente tiene distimia?: -","nel" if(trastorno[0][1]==0) else "si")
			
			print("El paciente tiene melancolico?: -","nel" if(tipo_trastorno[0][0]==0) else "si")
			print("El paciente tiene atipico?: -","nel" if(tipo_trastorno[0][1]==0) else "si")
			print("El paciente tiene catatonico?: -","nel" if(tipo_trastorno[0][2]==0) else "si")

			resultado_diagnostico = ResultadoDiagnostico()
			resultado_diagnostico.beck=nuevo_test
			resultado_diagnostico.Suicidio = False if suicidio_diagnostico==0 else True
			resultado_diagnostico.Depresion = False if trastorno[0][0]==0 else True
			resultado_diagnostico.Distimia = False if trastorno[0][1]==0 else True
			resultado_diagnostico.Melancolico = False if tipo_trastorno[0][0]==0 else True
			resultado_diagnostico.Atipico = False if tipo_trastorno[0][1]==0 else True
			resultado_diagnostico.Catatonico = False if tipo_trastorno[0][2]==0 else True
			resultado_diagnostico.save()

			resultados = {
				'Suicidio': False if suicidio_diagnostico==0 else True,
				'Depresion': False if trastorno[0][0]==0 else True,
				'Distimia': False if trastorno[0][1]==0 else True,
				'Melancolico': False if tipo_trastorno[0][0]==0 else True,
				'Atipico': False if tipo_trastorno[0][1]==0 else True,
				'Catatonico': False if tipo_trastorno[0][2]==0 else True,
			}

			return JsonResponse({'respuesta':True,'resultados':resultados})
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