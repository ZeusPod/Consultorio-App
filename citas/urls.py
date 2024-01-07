from django.urls import path
import citas.views as views

urlpatterns = [
   path('create_date/', views.create_date, name='create_date'),
   
]