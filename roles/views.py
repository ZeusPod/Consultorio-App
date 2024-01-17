from datetime import datetime
from django.shortcuts import get_object_or_404, render
import pytz
from roles.forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import User, RolesUsuario
from pacientes.models import Paciente
from citas.models import Cita
import logging


logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='roles:login')
def index(request):
    citas = Cita.objects.filter(status = False)
    citas_count = len(citas)
    pacientes = Paciente.objects.all()
    users = User.objects.all()

    return render(request, 'base/index.html', {'citas': citas, 'citas_count': citas_count , 'pacientes': pacientes, 'users': users})


# crear una cita desde el index 
def create_cita(request):   
    if request.method == 'POST':
        patient_id = request.POST.get('paciente')
        date_str = request.POST.get('dates_date')
        medic_id = request.POST.get('doctor')
        description = request.POST.get('description')
        hour_date = request.POST.get('horaCita')
        
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

        format_date_utc = datetime.combine(date_obj, datetime.strptime(hour_date, '%H:%M').time())
        # Obtener la zona horaria 'America/Caracas'
        caracas_tz = pytz.timezone('America/Caracas')

        # Convertir la fecha y hora a la zona horaria local
        format_date_local = caracas_tz.localize(format_date_utc)

        paciente = Paciente.objects.get(id=patient_id)
        medic = User.objects.get(id=medic_id)

        # Almacenar la fecha y hora en la base de datos
        cita = Cita.objects.create(patient=paciente, dates_date=format_date_local, hour_date=hour_date, medic=medic, description=description)
        cita.save()
        messages.success(request,'Cita agendada con exito')

        return redirect('roles:index')
    


### register ###
def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Usuario creado con exito')
                return redirect('roles:user_list')
            except Exception as e:
                messages.error(request, 'Error al crear usuario')
                logger.exception(e)
                return redirect('roles:register')
    else:
        form = CustomUserCreationForm()
    return render(request, 'roles/register.html', {'form': form})

### users list ###
@login_required(login_url='roles:login')
def user_list(request):
    users = User.objects.all()
    roles = RolesUsuario.objects.all()
    return render(request, 'roles/user_list.html', {'users': users , 'roles': roles})

### user update ###
@login_required(login_url='roles:login')
def user_update(request, pk):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        user = User.objects.get(id=pk)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.role = get_object_or_404(RolesUsuario, pk=role)

        user.save()
        messages.success(request, 'Usuario actualizado con exito')
        return redirect('roles:user_list')
    
    return redirect('roles:user_list')


### roles maintainer ###
@login_required(login_url='roles:login')
def roles_maintainer(request):
    roles = RolesUsuario.objects.all()
    return render(request, 'roles/roles_maintainer.html', {'roles': roles})

### roles create ###
@login_required(login_url='roles:login')
def roles_create(request):
    if request.method == 'POST':
        name = request.POST.get('rolName')
        # consultar si el rol ya existe
        if RolesUsuario.objects.filter(name=name).exists():
            messages.error(request, 'El rol ya existe')
            return redirect('roles:roles_maintainer')
        
        role = RolesUsuario(name=name)
        role.save()
        messages.success(request, 'Rol creado con exito')
        return redirect('roles:roles_maintainer')
    
    return redirect('roles:roles_maintainer')