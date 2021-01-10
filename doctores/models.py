from django.db import models

# Create your models here.
class Paciente(models.Model):
    email = models.EmailField(max_length=60, unique=True)
    birth_date = models.DateField()
    sex = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    civil_state = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    economical_situation  = models.CharField(max_length=50)

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
