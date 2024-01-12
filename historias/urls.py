from django.urls import path
import historias.views as views

urlpatterns = [
    path('historia/<int:pk>/', views.historia, name='historia'),
    ]