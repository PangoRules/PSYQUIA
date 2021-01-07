from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms
from django.http import JsonResponse, HttpResponse

def iniciar_sesion(request):
    form = forms.LoginForm
    context = {'form':form}
    return render(request, "main/iniciar_sesion.html",context)

"""
Esta funcion se encarga de los registros de los usuarios, si el metodo que esta recibiendo es POST
procede a registrar al usuario en caso de que el formulario este valido. De no ser un metodo POST el
que llamo a la funcion, simplemente retorna el archivo con el formulario a llenar para registrarse
"""
def registrarse(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'respuesta':True})
        #Esto sucedera cuando el formulario no sea validado de manera correcta. Falta el else y su respectivo bloque de codigo 
        else:
            return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})         
    context = {'form':form}
    return render(request, "main/registrarse.html",context)

def olvide_contra(request):
	return render(request, "main/olvide_contraseña.html")
