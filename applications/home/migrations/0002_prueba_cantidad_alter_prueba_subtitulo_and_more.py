# Generated by Django 4.1.4 on 2023-01-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='cantidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prueba',
            name='subtitulo',
            field=models.CharField(max_length=50, verbose_name='subtitulo'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
    ]
