from django.urls import path
import roles.views as views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register, name='register'),
    path('login/', LoginView.as_view(template_name='roles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_update/<int:pk>/', views.user_update, name='user_update'),
    path('roles_maintainer/', views.roles_maintainer, name='roles_maintainer'),
    path('roles_create/', views.roles_create, name='roles_create'),
    path('create_cita/' , views.create_cita, name='create_cita'),
    
]