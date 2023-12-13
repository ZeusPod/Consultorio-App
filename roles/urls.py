from django.urls import path
import roles.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register, name='register'),
    path('user_list/', views.user_list, name='user_list'),
]