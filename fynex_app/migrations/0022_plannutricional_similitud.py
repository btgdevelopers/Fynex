# Generated by Django 3.1.4 on 2021-03-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fynex_app', '0021_remove_mensaje_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannutricional',
            name='similitud',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
