from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import forms

# Create your views here.

def docDashboard(request):
	return render(request, "doctor/dashboard.html")

def docTest(request):
	return render(request, "doctor/test.html")

def docBeck(request):
	return render(request, "doctor/beck.html")

def docRegPaciente(request):
	form = forms.RegistrarPacienteForm()
	if request.method == 'POST':
		form = forms.RegistrarPacienteForm(request.POST)
		if form.is_valid():
			#form.save()
			return JsonResponse({'respuesta':True})
		else:
			return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})
	context = {'form':form}
	return render(request, "doctor/registrarpaciente.html",context)

def docCasoDistimico(request):
	return render(request, "doctor/casodistimico.html")

def docCasoDepresivo(request):
	return render(request, "doctor/casodepresivo.html")