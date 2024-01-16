"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'roles/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name = 'roles/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/', PasswordResetView.as_view(template_name = 'roles/password_reset.html'), name='password_reset'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'roles/password_reset_complete.html'), name='password_reset_complete'),
    path('', include(('roles.urls', 'roles'), namespace='roles')),
    path('pacientes/', include(('pacientes.urls', 'pacientes'), namespace='pacientes')),
    path('citas/', include(('citas.urls', 'citas'), namespace='citas')),
    path('historias/', include(('historias.urls', 'historias'), namespace='historias')),
    path('contactos/', include(('contactos.urls', 'contactos'), namespace='contactos')),
]
