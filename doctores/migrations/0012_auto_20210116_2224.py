# Generated by Django 3.1.2 on 2021-01-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0011_auto_20210116_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
