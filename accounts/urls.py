from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, register
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_request, name="login"),
    path('signup/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar_avatar'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='accounts/cambiar_password.html', success_url='/accounts/perfil/'), name='cambiar_password'),
]