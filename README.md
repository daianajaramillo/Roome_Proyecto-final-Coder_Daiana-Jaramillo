# TuPrimeraPagina-Jaramillo


# Instrucciones de prueba
1. Clonar el repositorio e ingresar a la carpeta
2. Activar el entorno virtual: .venv\Scripts\activate
3. Ejecutar migraciones: python manage.py migrate
4. Iniciar el servidor: python manage.py runserver


# Funcionalidades y ubicacion
El proyecto cuenta con tres modelos principales con sus respectivos formularios de carga y un buscador:

Alojamientos: Permite registrar nuevas propiedades (nombre, ciudad, precio y capacidad)
Ubicación: /alojamiento/

Anfitriones: Permite cargar datos de los anfitriones propiedades
Ubicación: /anfitrion/

Reservas: Permite registrar una estadía definiendo el viajero, fechas y cantidad de huéspedes
Ubicación: /reserva/

Buscador: Filtra alojamientos existentes por el nombre de la ciudad
Ubicación: /buscarAlojamiento/
