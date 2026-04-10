

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from .forms import MiFormularioDeRegistro, AvatarForm
from .models import Avatar
from django.contrib import messages


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect("inicio") 
    
    form = AuthenticationForm()
    form.fields['username'].label = "Nombre de usuario"
    form.fields['password'].label = "Contraseña"
    return render(request, "accounts/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = MiFormularioDeRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}! Tu cuenta fue creada con éxito.")
            return redirect("inicio")
        else:
            messages.error(request, "Error en el registro. Por favor, corregí los errores marcados abajo.")
    else:
        form = MiFormularioDeRegistro()
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    usuario = request.user
    perfil, created = Avatar.objects.get_or_create(user=usuario)
    
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.save()
        
        perfil.bio = request.POST.get('bio')
        perfil.cumpleanios = request.POST.get('cumpleanios') if request.POST.get('cumpleanios') else None
        perfil.save()
        
        messages.success(request, "¡Perfil actualizado con éxito!")
        return redirect('inicio')
    
    return render(request, 'accounts/perfil.html', {'usuario': usuario, 'perfil': perfil})

@login_required 
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect("editar_perfil") 
    else:
        form = AvatarForm()
    return render(request, "accounts/agregar_avatar.html", {"form": form})