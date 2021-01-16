from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from RedNeuDetecDepre.settings import EMAIL_HOST_USER
from . import forms
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from .decorators import not_authenticated, authenticated_user

@authenticated_user
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('DocDashboard')
        else:
            messages.error(request, 'Su correo o contraseña no coinciden')
    context = {}
    return render(request, "main/iniciar_sesion.html",context)

@not_authenticated
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Se ha cerrado su sesión con exito!')
    return redirect('PaginaFormIniciarSesion')

"""
Esta funcion se encarga de los registros de los usuarios, si el metodo que esta recibiendo es POST
procede a registrar al usuario en caso de que el formulario este valido. De no ser un metodo POST el
que llamo a la funcion, simplemente retorna el archivo con el formulario a llenar para registrarse
"""

@authenticated_user
def registrarse(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            send_mail(
                'Aviso de nuevo usuario',
                'Favor de revisar el nuevo usuario y activar su cuenta', 
                EMAIL_HOST_USER, 
                ['animasdelmundo2@gmail.com'], 
                fail_silently=False)
            form.save()
            return JsonResponse({'respuesta':True})
        #Esto sucedera cuando el formulario no sea validado de manera correcta. Falta el else y su respectivo bloque de codigo 
        else:
            return JsonResponse({'respuesta':False,'errores':dict(form.errors.items())})         
    context = {'form':form}
    return render(request, "main/registrarse.html",context)

@authenticated_user
def olvide_contra(request):
	return render(request, "main/olvide_contraseña.html")
