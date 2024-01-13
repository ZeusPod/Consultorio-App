from django.urls import path
import contactos.views as views

urlpatterns = [
    path('', views.contactos , name='contactos'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
]