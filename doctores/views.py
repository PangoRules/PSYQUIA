from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def docDashboard(request):
	return render(request, "doctor/dashboard.html")

def docTest(request):
	return render(request, "doctor/test.html")

def docBeck(request):
	return render(request, "doctor/beck.html")

def docRegPaciente(request):
	return render(request, "doctor/registrarpaciente.html")