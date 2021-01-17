from django.http import HttpResponse
from django.shortcuts import redirect

def not_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('PaginaFormIniciarSesion')
        else:
            return view_func(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return wrapper_func

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('DocDashboard')
        else:
            return view_func(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return wrapper_func