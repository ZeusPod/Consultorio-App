from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User , RolesUsuario


admin.site.register(User, UserAdmin)
admin.site.register(RolesUsuario)
