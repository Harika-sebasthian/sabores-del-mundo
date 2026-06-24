from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sabores/', views.sabores, name='sabores'),
    path('contacto/', views.contacto, name='contacto'),
    path('api/consultas/', views.api_consultas, name='api_consultas'),
    path('gastronomia/', views.gastronomia_mundial, name='gastronomia'),
]