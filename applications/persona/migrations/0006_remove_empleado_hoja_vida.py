# Generated by Django 4.1.4 on 2023-01-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
    ]