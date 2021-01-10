from django.db import models

#Opciones para los pacinetes
sexo = (('1', 'Hombre'),('2', 'Mujer'))
estudio = (('1', 'Sin estudios'),('2', 'Secundaria o menor'),('3', 'Media Superior'),('4', 'Superior'),('5', 'Posgrado'))
ocupacion = (('1', 'Sin ocupación'),('2', 'Estudios'),('3', 'Amo(a) de casa'),('4', 'Empleado(a) de empresa'),('5', 'Oficio o técnico'),('6', 'Emprendedor(a)'),('7', 'Profesionista'))
civil = (('1', 'Soltero'),('2', 'Casado'),('3', 'Unión libre'),('4', 'Viudo'),('5', 'Divorciado'),('6', 'Separado'))
religionChoices = (('1', 'Ninguna'),('2', 'Católica'),('3', 'Cristiano'),('4', 'Adventista'),('5', 'Ateo/Agnóstico'),('6', 'Otro'))
situacion = (('0', 'Bajo'),('1', 'Medio-bajo'),('2', 'Mediano'),('3', 'Medio-alto'),('4', 'Alto'))

# Create your models here.
class Paciente(models.Model):
    email = models.EmailField(max_length=60, unique=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1,choices=sexo,default=1)
    name = models.CharField(max_length=60)
    study = models.CharField(max_length=1,choices=estudio,default=1)
    job = models.CharField(max_length=1,choices=ocupacion,default=1)
    civil_state = models.CharField(max_length=1,choices=civil,default=1)
    religion = models.CharField(max_length=1,choices=religionChoices,default=1)
    economical_situation  = models.CharField(max_length=1,choices=situacion,default=1)

    def __str__(self):
        return self.name

class Beck(models.Model):
    paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    tristeza = models.IntegerField()
    pesimismo = models.IntegerField()
    fracaso = models.IntegerField()
    placer = models.IntegerField()
    culpa = models.IntegerField()
    castigo = models.IntegerField()
    disconformidad = models.IntegerField()
    autocritica = models.IntegerField()
    llanto = models.IntegerField()
    agitacion = models.IntegerField()
    interes = models.IntegerField()
    indecision = models.IntegerField()
    desvalorizacion = models.IntegerField()
    energia = models.IntegerField()
    sueño = models.IntegerField()
    irritabilidad = models.IntegerField()
    apetito = models.IntegerField()
    concentracion = models.IntegerField()
    fatiga = models.IntegerField()
    sexo = models.IntegerField()
    
    def __str__(self):
        return self.paciente
