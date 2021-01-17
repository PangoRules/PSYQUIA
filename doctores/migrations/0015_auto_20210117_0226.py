# Generated by Django 3.1.2 on 2021-01-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0014_auto_20210117_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beck',
            name='apetito',
            field=models.CharField(choices=[('0', 'No he experimentado ningún cambio en mi apetito.'), ('1a', 'Mi apetito es un poco menor que lo habitual.'), ('1b', 'Mi apetito es un poco mayor que lo habitual.'), ('2a', 'Mi apetito es mucho menor que antes.'), ('2b', 'Mi apetito es mucho mayor que lo habitual.'), ('3a', 'No tengo apetito en absoluto.'), ('3b', 'Quiero comer todo el día.')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='beck',
            name='sueño',
            field=models.CharField(choices=[('0', 'No he experimentado ningún cambio en mis hábitos de sueño.'), ('1a', 'Duermo un poco más que lo habitual.'), ('1b', 'Duermo un poco menos que lo habitual.'), ('2a', 'Duermo mucho más que lo habitual.'), ('2b', 'Duermo mucho menos que lo habitual.'), ('3a', 'Duermo la mayor parte del día.'), ('3b', 'Me despierto 1-2 horas más temprano y no puedo volver a dormirme.')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='job',
            field=models.IntegerField(choices=[(0, 'Estudios'), (1, 'Amo(a) de casa'), (2, 'Empleado(a) de empresa'), (3, 'Sin ocupación'), (4, 'Oficio o técnico'), (5, 'Emprendedor(a)'), (6, 'Profesionista')], default=1),
        ),
    ]
