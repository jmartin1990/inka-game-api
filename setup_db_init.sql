-- setup_db_init.sql
-- Script de inicialización para Inka Game Shop - PostgreSQL 17

-- 1. Limpieza para reiniciar la tabla
DROP TABLE IF EXISTS videojuegos;

-- 1. Tabla de Productos (Videojuegos y Suscripciones)
CREATE TABLE IF NOT EXISTS videojuegos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,          -- Precio actual (ej: 19.00)
    precio_anterior DECIMAL(10, 2),          -- Precio tachado (ej: 40.00)
    imagen_url VARCHAR(255) NOT NULL,
    categoria VARCHAR(50) NOT NULL           -- 'Retro', 'Nuevo', 'Oferta'
);

-- 2. Tabla de Usuarios que se suscriben
CREATE TABLE IF NOT EXISTS suscriptores (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tabla de Mensajes de Soporte
CREATE TABLE IF NOT EXISTS mensajes_soporte (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(255),
    mensaje TEXT,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Tabla de Inventario
CREATE TABLE IF NOT EXISTS inventario (
    id SERIAL PRIMARY KEY,
    juego_id INTEGER,
    nombre_juego VARCHAR(100),
    fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Carga de datos reales (Sincronizado con tu tienda)
INSERT INTO videojuegos (nombre, precio, precio_anterior, imagen_url, categoria) VALUES 
('Zelda: Ocarina', 45.00, NULL, '/tienda/zelda-ocarina.png', 'Retro'),
('Mario Kart World', 80.00, NULL, '/tienda/mario-kart-world.png', 'Nuevo'),
('Metroid Prime', 50.00, NULL, '/tienda/metroid-prime.png', 'Nuevo'),
('Nintendo Switch 2', 470.00, NULL, '/tienda/nintendo-switch-2.png', 'Nuevo'),
('Pack Nintendo', 490.00, 590.00, '/tienda/ofertas/nintendo-switch-2-box.png', 'Oferta'),
('Super Oferta Gamer', 19.00, 40.00, '/tienda/ofertas/gaming-products-50-v2.png', 'Oferta');