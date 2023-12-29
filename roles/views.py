from django.shortcuts import render
from roles.forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import User
import logging


logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='roles:login')
def index(request):
    return render(request, 'base/index.html')



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


@login_required(login_url='roles:login')
def user_list(request):
    users = User.objects.all()
    return render(request, 'roles/user_list.html', {'users': users})