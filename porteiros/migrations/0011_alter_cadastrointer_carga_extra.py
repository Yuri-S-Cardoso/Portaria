# Generated by Django 4.2.1 on 2023-06-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0010_cadastrointer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrointer',
            name='carga_extra',
            field=models.CharField(max_length=5),
        ),
    ]