from django.urls import path
import pacientes.views as views

urlpatterns = [
    path('pacientes/', views.pacientes, name='list_pacientes'),
    path('create_paciente/', views.create_paciente, name='create_paciente'),
    path('update_paciente/<int:pk>/', views.update_paciente, name='update_paciente'),
]