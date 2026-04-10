# Roome - Plataforma de Alquiler de Alojamientos 🏠

Roome es una aplicación web inspirada en Airbnb, desarrollada como proyecto final para el curso de Python/Django. La plataforma permite a los usuarios buscar alojamientos, gestionar sus reservas y personalizar su perfil de viajero con una interfaz moderna y minimalista.

## ✨ Características Principales

* **Buscador Inteligente:** Filtro de alojamientos por ciudad directamente desde la página de inicio.
* **Catálogo de Propiedades:** Visualización de alojamientos mediante tarjetas (cards) con diseño premium, precios y fotos.
* **Gestión de Usuarios (Accounts):**
    * Registro de nuevos usuarios y sistema de Login/Logout.
    * Edición de perfil personalizada (Nombre, Apellido, Email, Bio y Fecha de Nacimiento).
    * Sistema de Avatares dinámicos utilizando la librería Pillow.
* **Sección "Mis Viajes":** Espacio privado donde cada usuario puede visualizar sus reservas confirmadas.
* **Diseño UI/UX:** Interfaz limpia con una paleta de colores profesional, tipografía Inter y navegación dinámica.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.12+ / Django 5.x
* **Base de Datos:** SQLite3 (Desarrollo)
* **Procesamiento de Imágenes:** Pillow
* **Frontend:** HTML5, CSS3 (Variables nativas), Django Templates
* **Control de Versiones:** Git / GitHub

## 🚀 Instalación y Uso Local

Sigue estos pasos para ejecutar el proyecto en tu computadora:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/daianajaramillo/Roome.git](https://github.com/daianajaramillo/Roome.git)
   cd Roome


**Crear y activar el entorno virtual**
python -m venv .venv
# En Windows:
.venv\Scripts\activate

**Instalar dependencias**
pip install -r requirements.txt

**Ejecutar migraciones y el servidor (http://127.0.0.1:8000)**
python manage.py migrate
python manage.py runserver


