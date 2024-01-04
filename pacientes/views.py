from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pacientes.forms import PacienteForm
from pacientes.models import Paciente
from django.contrib import messages

#### PACIENTES #####
### CREATE PACIENTE
@login_required(login_url='roles:login')
def create_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente registrado con exito')
            return redirect('pacientes:list_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/create_paciente.html', {'form': form})

#### LIST PACIENTES ####
@login_required(login_url='roles:login')
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/pacientes.html' , {'pacientes': pacientes})

#### UPDATE PACIENTE ####	
@login_required(login_url='roles:login')
def update_paciente(request, pk):
    pass