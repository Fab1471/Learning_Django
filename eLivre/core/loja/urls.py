from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lancamentos/', views.lancamentos, name='lancamentos'),
    path('masculino/', views.masculino, name='masculino'),
    path('feminino/', views.feminino, name='feminino'),
]
