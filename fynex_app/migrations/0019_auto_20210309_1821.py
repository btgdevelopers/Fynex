# Generated by Django 3.1.4 on 2021-03-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fynex_app', '0018_auto_20210301_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]