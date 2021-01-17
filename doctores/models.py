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
    birth_date = models.DateField(auto_now=False, auto_now_add=False,)
    sex = models.CharField(max_length=1,choices=sexo,default=1)
    name = models.CharField(max_length=60)
    study = models.CharField(max_length=1,choices=estudio,default=1)
    job = models.CharField(max_length=1,choices=ocupacion,default=1)
    civil_state = models.CharField(max_length=1,choices=civil,default=1)
    religion = models.CharField(max_length=1,choices=religionChoices,default=1)
    economical_situation  = models.CharField(max_length=1,choices=situacion,default=1)

    def __str__(self):
        return self.name

tristeza = (('0', 'No me siento triste.'),('1', 'Me siento triste gran parte del tiempo.'),('2', 'Me siento triste todo el tiempo.'),('3', 'Me siento tan triste o soy tan infeliz que no puedo soportarlo.'),)
pesimismo = (('0', 'No estoy desalentado respecto del mi futuro.'),('1', 'Me siento más desalentado respecto de mi futuro que lo que solía estarlo.'),('2', 'No espero que las cosas funcionen para mi.'),('3', 'Siento que no hay esperanza para mi futuro y que sólo puede empeora.'),)
fracaso = (('0', 'No me siento como un fracasado.'),('1', 'He fracasado más de lo que hubiera debido.'),('2', 'Cuando miro hacia atrás, veo muchos fracasos.'),('3', 'Siento que como persona soy un fracaso total.'),)
placer = (('0', 'Obtengo tanto placer como siempre por las cosas de las que disfruto.'),('1', 'No disfruto tanto de las cosas como solía hacerlo.'),('2', 'Obtengo muy poco placer de las cosas que solía disfrutar.'),('3', 'No puedo obtener ningún placer de las cosas de las que solía disfrutar.'),)
culpa = (('0', 'No me siento particularmente culpable.'),('1', 'Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho.'),('2', 'Me siento bastante culpable la mayor parte del tiempo.'),('3', 'Me siento culpable todo el tiempo.'),)
castigo = (('0', 'No siento que este siendo castigado.'),('1', 'Siento que tal vez pueda ser castigado.'),('2', 'Espero ser castigado.'),('3', 'Siento que estoy siendo castigado.'),)
disconformidad = (('0', 'Siento acerca de mi lo mismo que siempre.'),('1', 'He perdido la confianza en mí mismo.'),('2', 'Estoy decepcionado conmigo mismo.'),('3', 'No me gusto a mí mismo.'),)
autocritica = (('0', 'No me critico ni me culpo más de lo habitual.'),('1', 'Estoy más crítico conmigo mismo de lo que solía estarlo.'),('2', 'Me critico a mí mismo por todos mis errores.'),('3', 'Me culpo a mí mismo por todo lo malo que sucede.'),)
llanto = (('0', 'No lloro más de lo que solía hacerlo.'),('1', 'Lloro más de lo que solía hacerlo.'),('2', 'Lloro por cualquier pequeñez.'),('3', 'Siento ganas de llorar pero no puedo.'),)
agitacion = (('0', 'No estoy más inquieto o tenso que lo habitual.'),('1', 'Me siento más inquieto o tenso que lo habitual.'),('2', 'Estoy tan inquieto o agitado que me es difícil quedarme quieto.'),('3', 'Estoy tan inquieto o agitado que tengo que estar siempre en movimiento o haciendo algo.'),)
interes = (('0', 'No he perdido el interés en otras actividades o personas.'),('1', 'Estoy menos interesado que antes en otras personas o cosas.'),('2', 'He perdido casi todo el interés en otras personas o cosas.'),('3', 'Me es difícil interesarme por algo.'),)
indecision = (('0', 'Tomo mis propias decisiones tan bien como siempre.'),('1', 'Me resulta más difícil que de costumbre tomar decisiones.'),('2', 'Encuentro mucha más dificultad que antes para tomar decisiones.'),('3', 'Tengo problemas para tomar cualquier decisión.'),)
desvalorizacion = (('0', 'No siento que yo no sea valioso.'),('1', 'No me considero a mi mismo tan valioso y útil como solía considerarme.'),('2', 'Me siento menos valioso cuando me comparo con otros.'),('3', 'Siento que no valgo nada.'),)
energia = (('0', 'Tengo tanta energía como siempre.'),('1', 'Tengo menos energía que la que solía tener.'),('2', 'No tengo suficiente energía para hacer demasiado.'),('3', 'No tengo energía suficiente para hacer nada.'),)
sueño = (('0', 'No he experimentado ningún cambio en mis hábitos de sueño.'),('1a', 'Duermo un poco más que lo habitual.'),('1b', 'Duermo un poco menos que lo habitual.'),('2a', 'Duermo mucho más que lo habitual.'),('2b', 'Duermo mucho menos que lo habitual.'),('3a', 'Duermo la mayor parte del día.'),('3b', 'Me despierto 1-2 horas más temprano y no puedo volver a dormirme.'),)
irritabilidad = (('0', 'No estoy tan irritable que lo habitual.'),('1', 'Estoy más irritable que lo habitual.'),('2', 'Estoy mucho más irritable que lo habitual.'),('3', 'Estoy irritable todo el tiempo.'),)
apetito = (('0', 'No he experimentado ningún cambio en mi apetito.'),('1a', 'Mi apetito es un poco menor que lo habitual.'),('1b', 'Mi apetito es un poco mayor que lo habitual.'),('2a', 'Mi apetito es mucho menor que antes.'),('2b', 'Mi apetito es mucho mayor que lo habitual.'),('3a', 'No tengo apetito en absoluto.'),('3b', 'Quiero comer todo el día.'),)
concentracion = (('0', 'Puedo concentrarme tan bien como siempre.'),('1', 'No puedo concentrarme tan bien como habitualmente.'),('2', 'Me es difícil mantener la mente en algo por mucho tiempo.'),('3', 'Encuentro que no puedo concentrarme en nada.'),)
fatiga = (('0', 'No estoy más cansado o fatigado que lo habitual.'),('1', 'Me fatigo o me canso más fácilmente que lo habitual.'),('2', 'Estoy demasiado fatigado o cansado para hacer muchas de las cosas que solía hacer.'),('3', 'Estoy demasiado fatigado o cansado para hacer la mayoría de las cosas que solía hacer.'),)
sexo = (('0', 'No he notado ningún cambio reciente en mi interés por el sexo.'),('1', 'Estoy menos interesado en el sexo de lo que solía estarlo.'),('2', 'Estoy mucho menos interesado en el sexo.'),('3', 'He perdido completamente el interés en el sexo.'),)

class Beck(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    tristeza = models.CharField(max_length=1,choices=tristeza,default=1)
    pesimismo = models.CharField(max_length=1,choices=pesimismo,default=1)
    fracaso = models.CharField(max_length=1,choices=fracaso,default=1)
    placer = models.CharField(max_length=1,choices=placer,default=1)
    culpa = models.CharField(max_length=1,choices=culpa,default=1)
    castigo = models.CharField(max_length=1,choices=castigo,default=1)
    disconformidad = models.CharField(max_length=1,choices=disconformidad,default=1)
    autocritica = models.CharField(max_length=1,choices=autocritica,default=1)
    llanto = models.CharField(max_length=1,choices=llanto,default=1)
    agitacion = models.CharField(max_length=1,choices=agitacion,default=1)
    interes = models.CharField(max_length=1,choices=interes,default=1)
    indecision = models.CharField(max_length=1,choices=indecision,default=1)
    desvalorizacion = models.CharField(max_length=1,choices=desvalorizacion,default=1)
    energia = models.CharField(max_length=1,choices=energia,default=1)
    sueño = models.CharField(max_length=2,choices=sueño,default=1)
    irritabilidad = models.CharField(max_length=1,choices=irritabilidad,default=1)
    apetito = models.CharField(max_length=2,choices=apetito,default=1)
    concentracion = models.CharField(max_length=1,choices=concentracion,default=1)
    fatiga = models.CharField(max_length=1,choices=fatiga,default=1)
    sexo = models.CharField(max_length=1,choices=sexo,default=1)

    def __str__(self):
        return self.paciente.name
