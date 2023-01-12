from django.db import models

# Create your models here.


class Prueba(models.Model):
    titulo = models.CharField('titulo',max_length= 50)
    subtitulo = models.CharField('subtitulo' ,max_length=50)
    cantidad = models.IntegerField('cantidad')

    def __str__(self):
        return self.titulo+ '-' + self.subtitulo