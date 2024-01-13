from django.shortcuts import redirect, render
from .models import Contactos
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .form import ContatcForm
from django.contrib import messages
# Create your views here.


### lista de contactos
@login_required(login_url='roles:login')
def contactos(request):
    contactos = Contactos.objects.all()
    return render(request, 'contactos/contactos_list.html', {'contactos': contactos})

### crear contactos
@login_required(login_url='roles:login')
def create_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contactos.objects.create(name=name, email=email, phone=phone)
        messages.success(request, 'Contacto creado con exito')
        return redirect('contactos:contactos')
    

### editar contactos
@login_required(login_url='roles:login')
def edit_contact(request, pk):
    if request.method == 'POST':
        contact = get_object_or_404(Contactos, pk=pk)
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        messages.success(request, 'Contacto actualizado con exito')
        return redirect('contactos:contactos')

### eliminar contactos
@login_required(login_url='roles:login')
def delete_contact(request, pk):
        contact = get_object_or_404(Contactos, pk=pk)
        contact.delete()
        messages.success(request, 'Contacto eliminado con exito')
        return redirect('contactos:contactos')
    