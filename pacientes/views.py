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
    form = PacienteForm()
    return render(request, 'pacientes/pacientes.html' , {'pacientes': pacientes, 'form': form})

#### UPDATE PACIENTE ####	
@login_required(login_url='roles:login')
def update_paciente(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        identification = request.POST.get('identification')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        email = request.POST.get('email')

        paciente = Paciente.objects.get(id=pk)
        paciente.large_name = name
        paciente.identification = identification
        paciente.address = address
        paciente.phone = phone
        paciente.gender = gender
        paciente.email = email

        paciente.save()
        messages.success(request, 'Paciente actualizado con exito')
        return redirect('pacientes:list_pacientes')

    return redirect('pacientes:list_pacientes')

