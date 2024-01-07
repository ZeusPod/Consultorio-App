from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from .models import Cita
from roles.models import User
from pacientes.models import Paciente
from django.utils import timezone
from datetime import datetime
import pytz
# Create your views here.




def create_date(request):
    if request.method == 'POST':
        patient_id = request.POST.get('paciente')
        date_str = request.POST.get('dates_date')
        medic_id = request.POST.get('doctor')
        description = request.POST.get('description')
        hour_date = request.POST.get('hora_cita')
    
        # Convertir la cadena de fecha y hora en un objeto datetime
        format_date_utc = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

        # Obtener la zona horaria 'America/Caracas'
        caracas_tz = pytz.timezone('America/Caracas')

        # Convertir la fecha y hora a la zona horaria local
        format_date_local = caracas_tz.localize(format_date_utc)

        paciente = Paciente.objects.get(id=patient_id)
        medic = User.objects.get(id=medic_id)

        # Almacenar la fecha y hora en la base de datos
        cita = Cita.objects.create(patient=paciente, dates_date=format_date_local, hour_date=hour_date, medic=medic, description=description)
        cita.save()

        cita_data = {
            'id': cita.id,
            'patient': cita.patient.id,
            'dates_date': caracas_tz.normalize(cita.dates_date).strftime('%Y-%m-%dT%H:%M:%S'),  # Formato ISO 8601 para enviar al frontend
            'hour_date': cita.hour_date,
            'medic': cita.medic.id,
            'description': cita.description,
        }

        return JsonResponse({'success': True, 'message': 'Cita agendada con éxito', 'data': cita_data})
        
    pacientes = Paciente.objects.all()
    users = User.objects.all()
    citas = Cita.objects.filter(status=False).values(
        'id', 'patient', 'dates_date', 'hour_date', 'medic', 'modification_date', 'description', 'status'
    )

    return render(request, 'citas/citas_calendar.html', {'pacientes': pacientes, 'users': users, 'citas': list(citas)})