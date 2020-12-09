from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admonHome(request):
	return HttpResponse('Hola admon')