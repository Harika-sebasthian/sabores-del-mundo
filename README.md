# Sabores del Mundo — Programación Web II Segundo Parcial

Sitio web para restaurante de cocina fusión desarrollado con Python y Django.

## Tecnologías utilizadas
- Python 3.13
- Django 6.0
- SQLite (desarrollo) / PostgreSQL (producción)
- Django REST Framework
- HTML, CSS, JavaScript

## Páginas
- **Inicio** — Presentación del restaurante
- **Nuestros Sabores** — Galería de platos
- **Gastronomía Mundial** — Recetas en tiempo real desde TheMealDB
- **Contacto** — Formulario de reservas

## API Externa utilizada
- TheMealDB: https://www.themealdb.com/api/json/v1/1/search.php?s=

## API Propia
- Consultas: `/api/consultas/`

## Panel de Administración
- Registro: `/panel/registro/`
- Login: `/panel/login/`
- Dashboard: `/panel/dashboard/`

## Configuración local
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv .venv`
3. Activar entorno: `.\.venv\Scripts\Activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Migrar base de datos: `python manage.py migrate`
6. Correr servidor: `python manage.py runserver`

## Despliegue
- GitHub: https://github.com/Harika-sebasthian/sabores-del-mundo
- Render: [URL del sitio desplegado]