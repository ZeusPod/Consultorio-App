from django.db import models

# Create your models here.
class Paciente(models.Model):
    large_name = models.CharField(max_length=100)
    identification = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.large_name
    

class History(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    register_date = models.DateTimeField()
    history = models.TextField()
    diagnostic = models.TextField()
    notes = models.TextField()
    follow_up = models.TextField()
    treatment = models.TextField()


    def __str__(self):
        return self.paciente.large_name
