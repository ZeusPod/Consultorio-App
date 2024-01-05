from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models



class RolesUsuario(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    role = models.ForeignKey(RolesUsuario, on_delete=models.CASCADE, null=True , blank=True)
    email = models.EmailField()
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name='user_permissions_set')
    

