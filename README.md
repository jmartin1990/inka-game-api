🎮 Inka Game Shop - API Backend
Este es el motor central (Backend) del ecosistema Inka Game Shop. Una API robusta construida con FastAPI y PostgreSQL 17 que gestiona el catálogo de videojuegos, las suscripciones de ofertas, el inventario de usuarios y los mensajes de soporte.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.12+

Framework: FastAPI (Moderno, rápido y basado en tipado).

Base de Datos: PostgreSQL 17 (Relacional).

ORM: SQLAlchemy (Gestión de base de datos mediante objetos).

Documentación: Swagger UI (Generada automáticamente).

📋 Requisitos del Proyecto
Este proyecto cumple con los 3 puntos clave solicitados + 2 extras

Entorno Virtual: Configurado y gestionado con venv.

Arquitectura API: Endpoints para juegos, suscripciones, soporte e inventario. Incluye script setup_db_init.sql.

Pruebas: Totalmente funcional y testeado mediante Swagger UI.

Frontend: Integración completa con cliente en Next.js.

Persistencia: Implementación estricta en PostgreSQL 17.

🚀 Guía de Instalación y Uso

1. Preparar el Entorno
   Desde la terminal en la carpeta raíz del proyecto:

# Crear entorno virtual

python -m venv venv

# Activar entorno (Windows)

source venv/Scripts/activate

# Instalar todas las dependencias necesarias

pip install -r requirements.txt 2. Inicializar la Base de Datos
Asegúrate de tener instalado PostgreSQL 17.

Crea una base de datos llamada inka_db.

Ejecuta el script contenido en el archivo setup_db_init.sql en tu herramienta de gestión (pgAdmin 4 o Query Tool) para crear las tablas y cargar los datos iniciales.

3. Ejecutar el Servidor
   Inicia la API en modo desarrollo:

fastapi dev
La API estará disponible en: http://127.0.0.1:8000

📖 Documentación de la API
Una vez encendido el servidor, puedes acceder a la documentación interactiva (Swagger) para probar todos los endpoints:
👉 http://127.0.0.1:8000/docs

📂 Estructura de Archivos
main.py: Punto de entrada de la aplicación y definición de rutas.

models.py: Definición de las tablas de la base de datos (SQLAlchemy).

database.py: Configuración de la conexión a PostgreSQL.

setup_db_init.sql: Script SQL para la creación e inicialización de la DB.

requirements.txt: Lista completa de dependencias y versiones.

💡 Nota de Integración
Para que el ecosistema funcione completo, recuerda tener corriendo simultáneamente el servidor de Next.js en el puerto 3000. La API tiene configurado el middleware CORS para permitir la comunicación segura entre ambos.

## 🔗 Ecosistema Completo (Full Stack)

Este repositorio contiene exclusivamente la **API (Backend)**. Para disfrutar de la experiencia completa de la tienda, con su interfaz visual, animaciones y gestión de inventario en tiempo real, es **imprescindible** descargar y ejecutar el frontend:

👉 **Frontend UI:** [inka-game-shop](https://github.com/jmartin1990/inka-game-shop)

### ⚙️ Cómo trabajan juntos:

1. El **Backend** (este repositorio) gestiona la base de datos PostgreSQL 17 y expone los datos en el puerto `8000`.
2. El **Frontend** (Next.js) consume esos datos y los muestra al usuario en el puerto `3000`.
3. Ambos deben estar ejecutándose simultáneamente para que las funcionalidades de "Añadir al Inventario" y "Suscripción" se reflejen en la base de datos.
