# Generated by Django 3.1.4 on 2021-01-19 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fynex_app', '0012_auto_20210119_1232'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recomendadormemoria',
            unique_together={('user1', 'user2')},
        ),
    ]