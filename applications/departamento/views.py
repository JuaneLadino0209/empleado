from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm

# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('**********estamos en el form valid**************')

        depa = Departamento(
            name = form.cleaned_data['departament'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        Empleado.objects.create(
            first_name = name,
            last_name = last_name,
            job='1',
            departament = depa
        )


        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'
