from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        (0, 'ADMINISTRADOR'),
        (1, 'SUPERVISOR'),
        (2, 'MEDICO'),
        (3, 'ASISTENTE'),
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True)
    email = models.EmailField()
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name='user_permissions_set')