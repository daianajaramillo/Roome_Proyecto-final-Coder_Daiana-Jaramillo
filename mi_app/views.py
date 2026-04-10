from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from .forms import AvatarForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Alojamiento, Anfitrion, Reserva
from .forms import AlojamientoForm, AnfitrionForm, ReservaForm
from accounts.models import Avatar
from django.contrib import messages

def inicio(request):
    lista_alojamientos = Alojamiento.objects.all()
    return render(request, "mi_app/index.html", {"alojamientos": lista_alojamientos})

class SoloDuenioMixin(UserPassesTestMixin):
    def test_func(self):
        alojamiento = self.get_object()
        return self.request.user == alojamiento.anfitrion or self.request.user.is_superuser
    
# Vistas basadas en clases para Alojamiento
class AlojamientoList(ListView):
    model = Alojamiento
    template_name = "mi_app/alojamiento_list.html"
    context_object_name = "alojamientos"

class AlojamientoDetail(DetailView):
    model = Alojamiento
    template_name = "mi_app/alojamiento_detalle.html"

class AlojamientoCreate(LoginRequiredMixin, CreateView):
    model = Alojamiento
    form_class = AlojamientoForm
    template_name = "mi_app/form_alojamiento.html"
    success_url = reverse_lazy('alojamiento_list')

    def form_valid(self, form):
        alojamiento = form.save(commit=False)
        alojamiento.anfitrion = self.request.user
        alojamiento.save()
        return super().form_valid(form)

class AlojamientoUpdate(LoginRequiredMixin, SoloDuenioMixin, UpdateView):
    model = Alojamiento
    form_class = AlojamientoForm  
    template_name = "mi_app/form_alojamiento.html"
    success_url = reverse_lazy('alojamiento_list')

class AlojamientoDelete(LoginRequiredMixin, SoloDuenioMixin, DeleteView):
    model = Alojamiento
    template_name = "mi_app/alojamiento_confirm_delete.html"
    success_url = reverse_lazy('alojamiento_list')

@login_required
def form_anfitrion(request):
    if request.method == "POST":
        formulario = AnfitrionForm(request.POST)
        if formulario.is_valid():
            formulario.save() 
            return render(request, "mi_app/index.html", {"mensaje": "Anfitrión guardado correctamente"})
    else:
        formulario = AnfitrionForm()
    return render(request, "mi_app/form_anfitrion.html", {"mi_form": formulario, "titulo": "Cargar Anfitrión"})

@login_required 
def form_reserva(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)
    
    if request.method == "POST":
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            reserva = formulario.save(commit=False)
            reserva.alojamiento = alojamiento 
            reserva.usuario = request.user
            reserva.save()
            
            messages.success(request, f"¡Reserva realizada con éxito!")
        
            return redirect("alojamiento_list") 
        else:
            messages.error(request, "Hubo un error en los datos. Revisá las fechas.")
    else:
        formulario = ReservaForm()
        
    return render(request, "mi_app/form_reserva.html", {"mi_form": formulario, "alojamiento": alojamiento})

def buscar_alojamiento(request):
    ciudad_buscada = request.GET.get("ciudad")
    if ciudad_buscada:
        resultados = Alojamiento.objects.filter(ciudad__icontains=ciudad_buscada)
        return render(request, "mi_app/buscar_alojamiento.html", {
            "alojamientos": resultados, 
            "ciudad": ciudad_buscada,
            "busqueda_realizada": True
        })
    return render(request, "mi_app/buscar_alojamiento.html", {"busqueda_realizada": False})

def about(request):
    return render(request, "mi_app/about.html")


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES) 
        if form.is_valid():
            
            Avatar.objects.filter(user=request.user).delete()
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect("inicio")
    else:
        form = AvatarForm()
    return render(request, "mi_app/agregar_avatar.html", {"form": form})


@login_required
def mis_viajes(request):
    reservas = Reserva.objects.filter(usuario=request.user)

    return render(request, 'mi_app/mis_viajes.html', {'reservas': reservas})