from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.inicio, name='inicio'),

    path('alojamiento/lista/', views.AlojamientoList.as_view(), name='alojamiento_list'),
    
    path('alojamiento/<int:pk>/', views.AlojamientoDetail.as_view(), name='alojamiento_detalle'),
    
    path('alojamiento/crear/', views.AlojamientoCreate.as_view(), name='alojamiento_crear'),
    
    path('alojamiento/editar/<int:pk>/', views.AlojamientoUpdate.as_view(), name='alojamiento_editar'),
    
    path('alojamiento/borrar/<int:pk>/', views.AlojamientoDelete.as_view(), name='alojamiento_borrar'),

    path('anfitrion/nuevo/', views.form_anfitrion, name='form_anfitrion'),
    path('alojamiento/<int:alojamiento_id>/reservar/', views.form_reserva, name='crear_reserva'),
    path('buscar/', views.buscar_alojamiento, name='buscar_alojamiento'),
    path('about/', views.about, name='about'),
    path('agregar_avatar/', views.agregar_avatar, name='agregar_avatar'),
    path('mis-viajes/', views.mis_viajes, name='mis_viajes'),
]