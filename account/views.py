from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from RedNeuDetecDepre.settings import EMAIL_HOST_USER
from . import forms
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from .decorators import not_authenticated, authenticated_user
from account.models import Account

@authenticated_user
def iniciar_sesion(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		usuario = authenticate(request, email=email, password=password)
		if usuario is not None:
			login(request,usuario)
			print(usuario.is_superuser)
			if usuario.is_superuser:
				return redirect('/admin/')
			else:
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
            correos_admins = Account.objects.values_list('email',flat=True).filter(is_superuser=True)
            doctor_correo = form.cleaned_data['email']
            doctor_cedula = form.cleaned_data['cedula']
            doctor_nombre = form.cleaned_data['nombres'] +' ' +form.cleaned_data['apellidos']
            send_mail(
                'Aviso de nuevo usuario',
                'Favor de revisar el nuevo usuario y activar su cuenta. Nombre Completo: '+doctor_nombre+', Correo: '+doctor_correo+', Cedula: '+doctor_cedula+'. Validar la cedula en https://cedulaprofesional.sep.gob.mx/cedula/presidencia/indexAvanzada.action', 
                EMAIL_HOST_USER, 
                correos_admins, 
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
	if request.method == 'POST':
		email = request.POST.get('email')
		if Account.objects.filter(email=email):
			correos_admins = Account.objects.values_list('email',flat=True).filter(is_superuser=True)
			send_mail(
					'USUARIO SOLICITA CAMBIO DE CONTRASEÑA',
					'Favor de contactar al usuario con correo: '+email+'. Para el cambio.', 
					EMAIL_HOST_USER, 
					correos_admins, 
					fail_silently=False)
			messages.success(request, 'Un administrador en breves se pondra en contacto con usted')
		else:
			messages.error(request, 'Su correo no exite en la base de datos')
	return render(request, "main/olvide_contraseña.html")
