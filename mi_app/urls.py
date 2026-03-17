from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alojamiento/', views.form_alojamiento, name='form_alojamiento'),
    path('anfitrion/', views.form_anfitrion, name='form_anfitrion'),
    path('reserva/', views.form_reserva, name='form_reserva'),
    path('buscarAlojamiento/', views.buscar_alojamiento, name='buscar_alojamiento'),
]