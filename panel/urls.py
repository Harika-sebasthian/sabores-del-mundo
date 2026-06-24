from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro,         name='registro'),
    path('validar/',  views.validar,           name='validar'),
    path('login/',    views.login_panel,       name='login_panel'),
    path('logout/',   views.logout_panel,      name='logout_panel'),
    path('dashboard/', views.dashboard,        name='dashboard'),
    path('eliminar/<int:id>/', views.eliminar_consulta, name='eliminar_consulta'),
]