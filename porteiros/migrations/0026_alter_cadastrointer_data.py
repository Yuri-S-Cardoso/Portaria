# Generated by Django 4.2.1 on 2023-07-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0025_rename_placa_cadastrointerentrada_placa_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrointer',
            name='data',
            field=models.DateField(),
        ),
    ]
