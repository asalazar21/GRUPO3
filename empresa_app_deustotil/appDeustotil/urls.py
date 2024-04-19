from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),

    path('proyectos', views.ProyectoListView.as_view(), name='index_proyectos'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='detail_proyectos'),
    path('proyectos/<int:pk>/borrar/', views.ProyectoDeleteView.as_view(), name='delete_proyectos'),
    
    path('tareas', views.TareaListView.as_view(), name='index_proyectos'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='detail_proyectos'),
    path('tareas/<int:pk>/borrar/', views.TareaDeleteView.as_view(), name='delete_proyectos'),
    
    path('empleados', views.EmpleadoListView.as_view(), name='index_proyectos'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='detail_proyectos'),
    path('empleados/<int:pk>/borrar/', views.EmpleadoDeleteView.as_view(), name='delete_proyectos'),

    
   
]