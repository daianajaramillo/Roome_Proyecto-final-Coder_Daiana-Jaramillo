
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class MiFormularioDeRegistro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ("username", "email")
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': 'Solo combinaciones de letras y números.',
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        labels = {
            'imagen': 'Foto de perfil',
        }