"""RedNeuDetecDepre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('doc/dashboard',views.docDashboard, name="DocDashboard"),
    path('doc/test',views.docTest, name="DocTest"),
    path('doc/becktest',views.docBeck, name="DocBeckTest"),
    path('doc/registrarpaciente',views.docRegPaciente, name="DocRegPac"),
    path('doc/casos_distimicos', views.docCasoDistimico, name="DocCasoDistimico"),
    path('doc/casos_depresivos', views.docCasoDepresivo, name="DocCasoDepresivo"),

    path('doc/get_datos_paciente',views.docGetDatosPaciente),
    path('doc/editar_paciente',views.docEditarPaciente),
    path('doc/get_test_beck', views.docGetTestBeck),
]
