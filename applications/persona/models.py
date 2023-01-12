from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'        

    def __str__(self):
        return str(self.id) + '-' + self.habilidad



# Create your models here.

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO')
    )

    first_name = models.CharField('firt_name', max_length=60)
    last_name = models.CharField('last_name', max_length=60)
    full_name = models.CharField(
        'full_name',
        max_length=120,
        blank=True
    )
    job = models.CharField('job', max_length=1, choices=JOB_CHOICES)
    departament = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='persona', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    # hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        # ordering  = ['id']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


