import datetime
from django.shortcuts import render
from .models import Historia
from pacientes.models import Paciente
from citas.models import Cita  
from historias.models import Historia
from django.contrib import messages
# Create your views here.

def historia(request, pk):
    if request.method == 'POST':
        paciente = Paciente.objects.get(id=pk)
        historia = Historia.objects.filter(patient=paciente).first()
        """ filtramos la cita por paciente y que el status sea falso """
        cita = Cita.objects.filter(patient=paciente, status=False).first()
        if historia:
            historia.medic = request.user
            historia.anamnesis = request.POST.get('anamnesis')
            historia.treatment = request.POST.get('treatment')
            historia.diagnostic = request.POST.get('diagnostic')
            historia.modification_date = datetime.datetime.now()
            historia.save()
            cita.status = True
            cita.save()
            messages.success(request, 'Historia actualizada con exito')
            return render(request, 'historias/historias.html', {'paciente': paciente, 'historia': historia})
        else:
            Historia.objects.create(patient=paciente, register_date= datetime.datetime.now(), medic=request.user, anamnesis=request.POST.get('anamnesis'), diagnostic=request.POST.get('diagnostic'), treatment=request.POST.get('treatment'), modification_date= datetime.datetime.now())
            messages.success(request, 'Historia creada con exito')
            return render(request, 'historias/historias.html', {'paciente': paciente})


    paciente = Paciente.objects.get(id=pk)
    historia = Historia.objects.filter(patient=paciente).first()
    
    return render(request, 'historias/historias.html', {'paciente': paciente, 'historia': historia})


def update_historia(request, pk):
    pass


def delete_historia(request, pk):
    pass