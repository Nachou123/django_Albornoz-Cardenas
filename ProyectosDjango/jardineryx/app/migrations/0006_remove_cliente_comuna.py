# Generated by Django 4.0.5 on 2022-06-29 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_cliente_apellido_cliente_comuna_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='comuna',
        ),
    ]
