from pydantic import BaseModel, Field, EmailStr, SecretStr, ConfigDict
from typing import Optional


class Usuarios(BaseModel):
    id: Optional[int] = None
    nombre:str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    rol: str = Field(default="2")
    
    model_config = ConfigDict(from_attributes=True)

#    class Config:
#        schema_extra = {
#            "example": {
#                "id": 1,
#                "nombre": "Elian",
#                "email": "elianmaineri@gmail.com",
#                "password": "Hola1234",
#                "rol": "Administrador | Cliente"
#            }
#        }

