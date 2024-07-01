from pydantic import BaseModel, Field, EmailStr, SecretStr, ConfigDict
from typing import Optional
from fastapi import FastAPI, status, Query, File, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel,EmailStr,Field, SecretStr, PositiveInt, field_validator
from datetime import date
from typing import List, Optional, Annotated
from passlib.context import CryptContext
from fastapi import UploadFile
from fastapi.responses import FileResponse
import os
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import shutil
import secrets

class UsuarioPass(BaseModel):
    id: Optional[int] = None
    nombre:str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    rol: str = 'Cliente'
    @field_validator('rol')
    def validar_rol(cls, v: str) -> str:
        rol_valido = v.upper()
        if rol_valido not in ("CLIENTE", "ADMINISTRADOR"):
            raise ValueError("El valor del campo 'rol' debe ser 'Cliente' o 'Administrador'.")
        return rol_valido.capitalize()
    
    model_config = ConfigDict(from_attributes=True)

class Usuarios(UsuarioPass):
    password: SecretStr 
    @field_validator('password')
    def validarPassword(cls, password:SecretStr)-> str :
        v = password.get_secret_value()
        
        if not any(char.isdigit() for char in v):
            raise HTTPException(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                detail="La contraseña debe contener al menos un número.")
        
        if not any(char.isalpha() for char in v):
            raise HTTPException(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                detail="La contraseña debe contener al menos una letra.")
        
        return v


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

