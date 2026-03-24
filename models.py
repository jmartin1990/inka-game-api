from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func # Importamos func para usar las funciones de la base de datos
from database import Base

class Videojuego(Base):
    """
    Modelo para la tabla de videojuegos. 
    Sincronizado con el catálogo y las ofertas de Inka Game Shop.
    """
    __tablename__ = "videojuegos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    precio_anterior = Column(Numeric(10, 2), nullable=True) # Para mostrar ofertas tachadas
    imagen_url = Column(String(255), nullable=False)
    categoria = Column(String(50), nullable=False) # 'Retro', 'Nuevo' o 'Oferta'


class Suscriptor(Base):
    """
    Modelo para los clientes que se suscriben a la Super Oferta Gamer.
    """
    __tablename__ = "suscriptores"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    
    # Usamos server_default para que PostgreSQL 17 asigne la hora automáticamente
    fecha_registro = Column(DateTime, server_default=func.now())
    
class MensajeSoporte(Base):
    __tablename__ = "mensajes_soporte"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String)
    mensaje = Column(String)
    fecha_envio = Column(DateTime, server_default=func.now())
    
class Inventario(Base):
    __tablename__ = "inventario"
    id = Column(Integer, primary_key=True, index=True)
    juego_id = Column(Integer)
    nombre_juego = Column(String)
    fecha_agregado = Column(DateTime, server_default=func.now())