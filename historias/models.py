from django.db import models
from pacientes.models import Paciente
from roles.models import User

# Create your models here.
class Historia(models.Model):
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    register_date = models.DateField(auto_now_add=True)
    medic = models.ForeignKey(User, on_delete=models.CASCADE)
    anamnesis = models.TextField()
    diagnostic = models.TextField()
    treatment = models.TextField()
    modification_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.patient.large_name
    

