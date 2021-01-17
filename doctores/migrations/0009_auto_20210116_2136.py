# Generated by Django 3.1.2 on 2021-01-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0008_paciente_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beck',
            name='agitacion',
            field=models.CharField(choices=[(0, 'No estoy más inquieto o tenso que lo habitual.'), (1, 'Me siento más inquieto o tenso que lo habitual.'), (2, 'Estoy tan inquieto o agitado que me es difícil quedarme quieto.'), (3, 'Estoy tan inquieto o agitado que tengo que estar siempre en movimiento o haciendo algo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='apetito',
            field=models.CharField(choices=[(0, 'No he experimentado ningún cambio en mi apetito.'), ('1a', 'Mi apetito es un poco menor que lo habitual.'), ('1b', 'Mi apetito es un poco mayor que lo habitual.'), ('2a', 'Mi apetito es mucho menor que antes.'), ('2b', 'Mi apetito es mucho mayor que lo habitual.'), ('3a', 'No tengo apetito en absoluto.'), ('3b', 'Quiero comer todo el día.')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='beck',
            name='autocritica',
            field=models.CharField(choices=[(0, 'No me critico ni me culpo más de lo habitual.'), (1, 'Estoy más crítico conmigo mismo de lo que solía estarlo.'), (2, 'Me critico a mí mismo por todos mis errores.'), (3, 'Me culpo a mí mismo por todo lo malo que sucede.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='castigo',
            field=models.CharField(choices=[(0, 'No siento que este siendo castigado.'), (1, 'Siento que tal vez pueda ser castigado.'), (2, 'Espero ser castigado.'), (3, 'Siento que estoy siendo castigado.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='concentracion',
            field=models.CharField(choices=[(0, 'Puedo concentrarme tan bien como siempre.'), (1, 'No puedo concentrarme tan bien como habitualmente.'), (2, 'Me es difícil mantener la mente en algo por mucho tiempo.'), (3, 'Encuentro que no puedo concentrarme en nada.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='culpa',
            field=models.CharField(choices=[(0, 'No me siento particularmente culpable.'), (1, 'Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho.'), (2, 'Me siento bastante culpable la mayor parte del tiempo.'), (3, 'Me siento culpable todo el tiempo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='desvalorizacion',
            field=models.CharField(choices=[(0, 'No siento que yo no sea valioso.'), (1, 'No me considero a mi mismo tan valioso y útil como solía considerarme.'), (2, 'Me siento menos valioso cuando me comparo con otros.'), (3, 'Siento que no valgo nada.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='disconformidad',
            field=models.CharField(choices=[(0, 'Siento acerca de mi lo mismo que siempre.'), (1, 'He perdido la confianza en mí mismo.'), (2, 'Estoy decepcionado conmigo mismo.'), (3, 'No me gusto a mí mismo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='energia',
            field=models.CharField(choices=[(0, 'Tengo tanta energía como siempre.'), (1, 'Tengo menos energía que la que solía tener.'), (2, 'No tengo suficiente energía para hacer demasiado.'), (3, 'No tengo energía suficiente para hacer nada.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='fatiga',
            field=models.CharField(choices=[(0, 'No estoy más cansado o fatigado que lo habitual.'), (1, 'Me fatigo o me canso más fácilmente que lo habitual.'), (2, 'Estoy demasiado fatigado o cansado para hacer muchas de las cosas que solía hacer.'), (3, 'Estoy demasiado fatigado o cansado para hacer la mayoría de las cosas que solía hacer.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='fracaso',
            field=models.CharField(choices=[(0, 'No me siento como un fracasado.'), (1, 'He fracasado más de lo que hubiera debido.'), (2, 'Cuando miro hacia atrás, veo muchos fracasos.'), (3, 'Siento que como persona soy un fracaso total.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='indecision',
            field=models.CharField(choices=[(0, 'Tomo mis propias decisiones tan bien como siempre.'), (1, 'Me resulta más difícil que de costumbre tomar decisiones.'), (2, 'Encuentro mucha más dificultad que antes para tomar decisiones.'), (3, 'Tengo problemas para tomar cualquier decisión.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='interes',
            field=models.CharField(choices=[(0, 'No he perdido el interés en otras actividades o personas.'), (1, 'Estoy menos interesado que antes en otras personas o cosas.'), (2, 'He perdido casi todo el interés en otras personas o cosas.'), (3, 'Me es difícil interesarme por algo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='irritabilidad',
            field=models.CharField(choices=[(0, 'No estoy tan irritable que lo habitual.'), (1, 'Estoy más irritable que lo habitual.'), (2, 'Estoy mucho más irritable que lo habitual.'), (3, 'Estoy irritable todo el tiempo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='llanto',
            field=models.CharField(choices=[(0, 'No lloro más de lo que solía hacerlo.'), (1, 'Lloro más de lo que solía hacerlo.'), (2, 'Lloro por cualquier pequeñez.'), (3, 'Siento ganas de llorar pero no puedo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='pesimismo',
            field=models.CharField(choices=[(0, 'No estoy desalentado respecto del mi futuro.'), (1, 'Me siento más desalentado respecto de mi futuro que lo que solía estarlo.'), (2, 'No espero que las cosas funcionen para mi.'), (3, 'Siento que no hay esperanza para mi futuro y que sólo puede empeora.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='placer',
            field=models.CharField(choices=[(0, 'Obtengo tanto placer como siempre por las cosas de las que disfruto.'), (1, 'No disfruto tanto de las cosas como solía hacerlo.'), (2, 'Obtengo muy poco placer de las cosas que solía disfrutar.'), (3, 'No puedo obtener ningún placer de las cosas de las que solía disfrutar.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='sexo',
            field=models.CharField(choices=[(0, 'No he notado ningún cambio reciente en mi interés por el sexo.'), (1, 'Estoy menos interesado en el sexo de lo que solía estarlo.'), (2, 'Estoy mucho menos interesado en el sexo.'), (3, 'He perdido completamente el interés en el sexo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='beck',
            name='sueño',
            field=models.CharField(choices=[(0, 'No he experimentado ningún cambio en mis hábitos de sueño.'), ('1a', 'Duermo un poco más que lo habitual.'), ('1b', 'Duermo un poco menos que lo habitual.'), ('2a', 'Duermo mucho más que lo habitual.'), ('2b', 'Duermo mucho menos que lo habitual.'), ('3a', 'Duermo la mayor parte del día.'), ('3b', 'Me despierto 1-2 horas más temprano y no puedo volver a dormirme.')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='beck',
            name='tristeza',
            field=models.CharField(choices=[(0, 'No me siento triste.'), (1, 'Me siento triste gran parte del tiempo.'), (2, 'Me siento triste todo el tiempo.'), (3, 'Me siento tan triste o soy tan infeliz que no puedo soportarlo.')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='civil_state',
            field=models.CharField(choices=[(1, 'Soltero'), (2, 'Casado'), (3, 'Viudo'), (4, 'Divorciado'), (5, 'Unión libre'), (6, 'Separado')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='economical_situation',
            field=models.CharField(choices=[(0, 'Bajo'), (1, 'Medio-bajo'), (2, 'Mediano'), (3, 'Medio-alto'), (4, 'Alto')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='job',
            field=models.CharField(choices=[(1, 'Sin ocupación'), (2, 'Estudios'), (3, 'Amo(a) de casa'), (4, 'Empleado(a) de empresa'), (5, 'Oficio o técnico'), (6, 'Emprendedor(a)'), (7, 'Profesionista')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='religion',
            field=models.CharField(choices=[(1, 'Católica'), (2, 'Cristiano'), (3, 'Ateo/Agnóstico'), (4, 'Adventista'), (5, 'Otro'), (6, 'Ninguna')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sex',
            field=models.CharField(choices=[(1, 'Hombre'), (2, 'Mujer')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='study',
            field=models.CharField(choices=[(1, 'Sin estudios'), (2, 'Secundaria o menor'), (3, 'Media Superior'), (4, 'Superior'), (5, 'Posgrado')], default=1, max_length=1),
        ),
    ]