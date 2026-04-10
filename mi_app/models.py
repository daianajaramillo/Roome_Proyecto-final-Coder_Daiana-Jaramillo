from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del alojamiento")
    anfitrion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alojamientos', verbose_name="Anfitrión")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    precio_por_noche = models.IntegerField(verbose_name="Precio por noche")
    capacidad_personas = models.IntegerField(verbose_name="Capacidad (personas)")
    
    descripcion = RichTextField(null=True, blank=True, verbose_name="Descripción detallada")
    imagen = models.ImageField(upload_to='alojamientos/', null=True, blank=True, verbose_name="Imagen del lugar")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

    class Meta:
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"

class Anfitrion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    idiomas = models.CharField(max_length=100, verbose_name="Idiomas que habla") 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Anfitrión"
        verbose_name_plural = "Anfitriones"



class Reserva(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, related_name="reservas")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mis_reservas")
    
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")
    cantidad_huespedes = models.IntegerField(default=1, verbose_name="Cantidad de huéspedes")
    mensaje = models.TextField(blank=True, null=True, verbose_name="Mensaje para el anfitrión")

    def __str__(self):
        return f"Reserva de {self.usuario.username} en {self.alojamiento.nombre}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
