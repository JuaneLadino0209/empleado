from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('name', max_length=50, unique= True)
    shor_name = models.CharField('shor_name', max_length=20, blank=True, null = True)
    is_active = models.BooleanField('is_active', default = True)

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
