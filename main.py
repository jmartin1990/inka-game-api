from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
from database import get_db # <--- Importamos la función de tu database.py

app = FastAPI(title="Inka Game Shop API")

# IMPORTANTE: Permitir que Next.js se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/juegos", summary="Obtiene el catálogo ordenado por ID")
def obtener_juegos(db: Session = Depends(get_db)):
    # Añadimos .order_by(models.Videojuego.id) para que siempre respete el orden original
    return db.query(models.Videojuego).order_by(models.Videojuego.id).all()

@app.post("/suscribirse")
def registrar_email(email: str, db: Session = Depends(get_db)):
    nuevo = models.Suscriptor(email=email)
    db.add(nuevo)
    db.commit()
    return {"status": "success", "message": "Email guardado en PostgreSQL"}

@app.post("/contacto")
def enviar_mensaje(nombre: str, email: str, mensaje: str, db: Session = Depends(get_db)):
    # 1. Creamos el objeto
    nuevo = models.MensajeSoporte(nombre=nombre, email=email, mensaje=mensaje)
    
    # 2. Añadimos a la sesión de la DB
    db.add(nuevo)
    
    # 3. Guardamos los cambios permanentemente
    db.commit()
    
    # 4. Actualizamos el objeto para que Python sepa qué ID le puso PostgreSQL automáticamente
    db.refresh(nuevo)
    
    # 5. Respuesta que recibirá Next.js
    return {"status": "success", "mensaje": "Mensaje guardado en el soporte de Inka"}

@app.post("/inventario")
def añadir_al_inventario(juego_id: int, nombre: str, db: Session = Depends(get_db)):
    nuevo_item = models.Inventario(juego_id=juego_id, nombre_juego=nombre)
    db.add(nuevo_item)
    db.commit()
    return {"status": "success", "message": f"{nombre} añadido al inventario"}