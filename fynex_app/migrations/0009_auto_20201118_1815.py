# Generated by Django 3.1.2 on 2020-11-18 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fynex_app', '0008_variableseguimiento_obligatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannutricional',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
