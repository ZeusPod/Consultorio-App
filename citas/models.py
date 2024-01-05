from django.db import models
from pacientes.models import Paciente
from roles.models import User
# Create your models here.


class Cita(models.Model):
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dates_date = models.DateTimeField()
    medic = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    modification_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.patient.large_name
    