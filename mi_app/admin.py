from django.contrib import admin

# Register your models here.
from .models import Alojamiento, Anfitrion, Reserva

admin.site.register(Alojamiento)
admin.site.register(Anfitrion)
admin.site.register(Reserva)

