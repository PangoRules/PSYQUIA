from django.contrib import admin
from doctores.models import Paciente, Beck, ResultadoDiagnostico
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Beck)
admin.site.register(ResultadoDiagnostico)
