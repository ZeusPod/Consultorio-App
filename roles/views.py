from django.shortcuts import get_object_or_404, render
from roles.forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import User, RolesUsuario
from citas.models import Cita
import logging


logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='roles:login')
def index(request):
    citas = Cita.objects.filter(status = False)
    citas_count = len(citas)
    return render(request, 'base/index.html', {'citas': citas, 'citas_count': citas_count})


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