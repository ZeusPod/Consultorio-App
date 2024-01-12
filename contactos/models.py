from django.db import models

# Create your models here.
class Contactos(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank= True)
    phone = models.CharField(max_length =12, null= True , blank=True)


    def __str__(self) -> str:
        return self.name