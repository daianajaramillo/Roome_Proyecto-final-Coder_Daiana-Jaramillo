from django import forms
from .models import Alojamiento 
from ckeditor.widgets import CKEditorWidget
from accounts.models import Avatar
from .models import Reserva  

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = [
            'nombre', 
            'ciudad', 
            'precio_por_noche', 
            'capacidad_personas', 
            'descripcion', 
            'imagen'
        ]
        widgets = {
            'descripcion': CKEditorWidget(),
        }

class AnfitrionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    idiomas = forms.CharField(max_length=100)

class ReservaForm(forms.ModelForm): 
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin', 'cantidad_huespedes']
        
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

#Form para buscar en BD
class BuscarAlojamientoForm(forms.Form):
    ciudad = forms.CharField(max_length=100)

#Avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']