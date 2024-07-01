from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class PaquetesDeViaje(BaseModel):

    id: int
    destinoId: int
    nombre: str
    precio: float
    cupo: int
    fecha_inicio: date
    fecha_fin: date
    