from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )

# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de incio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name ='empleados'
    # model = Empleado

    def get_queryset(self):
        print('**************************')
        palabra_clave = self.request.GET.get("kword", '')        
        print('========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name ='empleados'
    model=Empleado
    

    # def get_queryset(self):
    #     print('**************************')
    #     palabra_clave = self.request.GET.get("kword", '')        
    #     print('========', palabra_clave)
    #     lista = Empleado.objects.filter(
    #         first_name__icontains=palabra_clave
    #     )
    #     return lista

class ListByAreaEmpleado(ListView):
    """ lista de empleados de un area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #el codigo que quiera
        area = self.kwargs['shorname']

        lista = Empleado.objects.filter(
            departament__shor_name = area
            )
        return lista

class ListEmpleadosByKwors(ListView):
    """ Lista Empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('**************************')
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):

        getId = self.request.GET.get('id', '1')
        empleado = Empleado.objects.get(id=getId)
        return empleado.habilidades.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Todo un proceso
        context['titulo'] = 'Empleado el mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    # fields = ('__all__')
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + '' + empleado.last_name
        empleado.save()
        print(empleado)

        return super(EmpleadoCreateView, self).form_valid(form)

    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departament',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*************METODO POST**********************')
        print('===============')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        print('*************METODO FORM VALID**********************')
        print('****************************************')

        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')








#============== HECHO ============================
# 1.- Listar todos los empleados de la empresa - check
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar los empleados por palabra clave
# 3.- Listar empleados por habilidad




# Create your views here.


