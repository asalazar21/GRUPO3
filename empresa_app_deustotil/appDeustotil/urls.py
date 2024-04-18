from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),

    path('tickets', views.ProyectoListView.as_view(), name='index_proyectos'),
    path('tickets/<int:pk>/', views.ProyectoDetailView.as_view(), name='detail_proyectos'),
    path('tickets/<int:pk>/borrar/', views.ProyectoDeleteView.as_view(), name='delete_proyectos'),
    
    path('tickets', views.TareaListView.as_view(), name='index_proyectos'),
    path('tickets/<int:pk>/', views.TareaDetailView.as_view(), name='detail_proyectos'),
    path('tickets/<int:pk>/borrar/', views.TareaDeleteView.as_view(), name='delete_proyectos'),
    
    path('tickets', views.EmpleadoListView.as_view(), name='index_proyectos'),
    path('tickets/<int:pk>/', views.EmpleadoDetailView.as_view(), name='detail_proyectos'),
    path('tickets/<int:pk>/borrar/', views.EmpleadoDeleteView.as_view(), name='delete_proyectos'),

   
]