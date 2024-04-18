from django.db import models

#Clase Proveedor referencia al campo proveedor de la clase Equipo
class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prioridad (models.Model):
    nombre = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.nombre

class Responsable (models.Model):
    nombre = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.nombre

class EstadoTarea (models.Model):
    nombre = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.nombre



#Clase Empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre + " " + self.dni
    

class Tarea(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)    #1-N MIRAR SI ES ASI!!!!!!!!
    nivel_prioridad =  models.ForeignKey(Prioridad, on_delete=models.CASCADE) #1-N MIRAR SI ES ASI!!!!!!!!
    estado_tarea =   models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)   #1-N MIRAR SI ES ASI!!!!!!!!
    notas = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nombre + " " + self.responsable


#Clase Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarea_a_realizar = models.ManyToManyField(Tarea.nombre)   #N-M MIRAR SI ES ASI!!!!!!!!
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE) #1-N MIRAR SI ES ASI!!!!!!!!
    
    def __str__(self):
        return self.nombre + " " + self.responsable + " " + self.presupuesto
    


