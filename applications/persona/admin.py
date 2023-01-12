from django.contrib import admin
from.models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departament',
        'job',
        'full_name',
        'id',
    )
    ordering = ('-id',)
    #
    def full_name(self, obj):
        #toda la operacion que necesite
        print(obj)

        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ('departament','job', 'habilidades')
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)