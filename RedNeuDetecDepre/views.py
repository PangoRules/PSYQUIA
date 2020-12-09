from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "main/home.html")

def iniciar_sesion(request):
	return render(request, "main/iniciar_sesion.html")

def registrarse(request):
	return render(request, "main/registrarse.html")

def olvide_contra(request):
	return render(request, "main/olvide_contraseña.html")