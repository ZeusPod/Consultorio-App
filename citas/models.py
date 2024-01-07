from django.db import models
from pacientes.models import Paciente
from roles.models import User
# Create your models here.


class Cita(models.Model):
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dates_date = models.DateTimeField()
    hour_date = models.TimeField(default='00:00')
    medic = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    modification_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Cita para {self.patient} con el Dr. {self.medic} el {self.dates_date} a las {self.hour_date}'
    