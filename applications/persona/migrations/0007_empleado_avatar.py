# Generated by Django 4.1.4 on 2023-01-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_remove_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
