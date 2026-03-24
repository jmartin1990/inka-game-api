# 🎮 Inka Game Shop - API Backend

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135.2-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql)

Este es el motor central (**Backend**) del ecosistema **Inka Game Shop**. Una API robusta diseñada para gestionar el catálogo de videojuegos, suscripciones de ofertas, inventario de usuarios y mensajería de soporte.

---

## 👤 Información del Proyecto

- **Autor:** Juan Campos
- **Stack:** `FastAPI`, `PostgreSQL 17`, `SQLAlchemy`, `Python 3.12+`
- **Deploy:** Local y GitHub (rama `main`)

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** `Python 3.12+`
- **Framework:** `FastAPI` (Moderno, rápido y basado en tipado).
- **Base de Datos:** `PostgreSQL 17` (Relacional).
- **ORM:** `SQLAlchemy` (Gestión de base de datos mediante objetos).
- **Documentación:** `Swagger UI` (Generada automáticamente).

---

## 📋 Requisitos del Proyecto (Checklist)

Este proyecto cumple estrictamente con los 5 puntos clave solicitados:

1.  ✅ **Entorno Virtual:** Configurado y gestionado con `venv`.
2.  ✅ **Arquitectura API:** Endpoints para juegos, suscripciones, soporte e inventario. Incluye script `setup_db_init.sql`.
3.  ✅ **Pruebas:** Totalmente funcional y testeado mediante **Swagger UI**.
4.  ✅ **Frontend:** Integración completa con cliente en **Next.js**.
5.  ✅ **Persistencia:** Implementación estricta en **PostgreSQL 17**.

---

## 🚀 Guía de Instalación y Uso

### 1. Preparar el Entorno

Ejecuta estos comandos desde la terminal en la carpeta raíz del proyecto:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno (Windows)
source venv/Scripts/activate

# Instalar todas las dependencias necesarias
pip install -r requirements.txt

```

### 2. Inicializar la Base de Datos

- Asegúrate de tener instalado PostgreSQL 17.

- Crea una base de datos llamada inka_db.

- Ejecuta el script contenido en el archivo setup_db_init.sql en tu herramienta de gestión (pgAdmin 4 o Query Tool) para crear las tablas y cargar los datos iniciales de la tienda.

### 3. Ejecutar el Servidor

Inicia la API en modo desarrollo:

```bash
fastapi dev

```

### La API estará disponible en: http://127.0.0.1:8000

## Documentación de la API

Una vez encendido el servidor, puedes acceder a la documentación interactiva para probar todos los endpoints en tiempo real:

### Swagger UI: http://127.0.0.1:8000/docs

## Estructura de Archivos

- main.py: Punto de entrada de la aplicación y definición de rutas.

- models.py: Definición de las tablas de la base de datos (SQLAlchemy).

- database.py: Configuración de la conexión a PostgreSQL.

- setup_db_init.sql: Script SQL para la creación e inicialización de la DB.

- requirements.txt: Lista completa de dependencias y versiones.

- .gitignore: Filtro para evitar subir archivos temporales (**pycache**, venv).

## Ecosistema Completo (Full Stack)

Este repositorio contiene exclusivamente la API (Backend). Para disfrutar de la experiencia completa de la tienda, es imprescindible ejecutar el frontend:

### Frontend UI: [inka-game-shop](https://github.com/jmartin1990/inka-game-shop)

## Ecosistema Completo (Full Stack)

1. Backend (API): Gestiona la lógica de negocio y la base de datos PostgreSQL 17 en el puerto 8000.

2. Frontend (Next.js): Consume los datos de la API y los presenta de forma visual en el puerto 3000.

3. CORS: La API tiene configurado el middleware de CORS para permitir peticiones seguras desde el origen de Next.js.
