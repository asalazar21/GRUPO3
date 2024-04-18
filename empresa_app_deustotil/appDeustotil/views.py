from django.shortcuts import render
from .models import Proyecto, Tarea, Empleado, Cliente, EstadoTarea, Prioridad, Responsable
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
# Create your views here.


class IndexListView(ListView):
    def get(self, request, *args, **kwargs):
        proyectos = Proyecto.objects.all()[:5]
        tareas = Tarea.objects.all()[:5]
        empleados = Empleado.objects.all()[:5]
        clientes = Cliente.objects.all()[:5]
        context = {'lista_proyectos': proyectos, 'lista_tareas': tareas, 'lista_empleados': empleados, 'lista_clientes': clientes}
        return render(request,'index.html', context)        #FALTA CREAR index.html
        

#LISTA DE TODOS LOS DATOS DE LAS 5 PRIMERAS TAREAS
class TareaListView(ListView):
    model = Tarea
    template_name = 'index_tareas.html'  #FALTA CREAR
    context_object_name = 'lista_tareas' #FALTA PONER IGUAL EN index_tareas.html
    # queryset = Proyecto.objects.order_by('nombre')  #¿poner aqui?
    paginate_by = 10


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html' #FALTA CREAR


class TareaDeleteView(DeleteView):
    model = Tarea
    success_url = reverse_lazy('index_tareas') #FALTA PONER IGUAL EN index_tareas.html
    
    
    
# ------------------


class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'index_proyectos.html'  #FALTA CREAR
    context_object_name = 'lista_proyectos' #FALTA PONER IGUAL EN index_proyectos.html
    paginate_by = 10
    # queryset = Proyecto.objects.order_by('nombre')  #¿poner aqui?



class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html' #FALTA CREAR


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('index_proyectos') #FALTA PONER IGUAL EN index_tareas.html



# ------------------

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'index_empleados.html'  #FALTA CREAR
    context_object_name = 'lista_empleados' #FALTA PONER IGUAL EN index_tareas.html
    paginate_by = 10
    # queryset = Proyecto.objects.order_by('dni')  #¿poner aqui? o 'dni'?


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html' #FALTA CREAR


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('index_empleados') #FALTA PONER IGUAL EN index_tareas.html
    
    

# ------------------