from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.Usuarios import Usuarios as UsuariosModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.UsuariosServices import UsuariosServices
from schemas.UsuariosSchemas import Usuarios
from passlib.context import CryptContext
from utils.jwt_manager import create_token


usuarios_router = APIRouter()

@usuarios_router.get('/ALL-USUARIOS', tags=['Usuarios'], response_model=List[Usuarios], status_code=200, dependencies=[Depends(JWTBearer())])
def get_all_usuarios():
    db = Session()
    usuarios = UsuariosServices(db).get_all_usuarios()
    if not usuarios:
        return JSONResponse(status_code=404, content={"message": "No se encontro ningun usuario"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuarios))

@usuarios_router.get('/ID-USUARIOS', tags=['Usuarios'], response_model=List[Usuarios], status_code=200, dependencies=[Depends(JWTBearer())])
def get_id_usuarios(id: int):
    db = Session()
    usuarios = UsuariosServices(db).get_id_usuarios(id)
    if not usuarios:
        return JSONResponse(status_code=404, content={"message": "No se encontro ningun usuario con ese id"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuarios))

@usuarios_router.get('/EMAIL-USUARIOS', tags=['Usuarios'], response_model=Usuarios, status_code=200, dependencies=[Depends(JWTBearer())])
def get_email_usuarios(email: str):
    db = Session()
    usuarios = UsuariosServices(db).get_email_usuarios(email)
    if not usuarios:
        return JSONResponse(status_code=404, content={"message": "No se encontro ningun usuario con ese email"})
    return JSONResponse(status_code=200, content=jsonable_encoder(usuarios))

@usuarios_router.post('/USUARIOS', tags=['Usuarios'], response_model=Usuarios, status_code=200, dependencies=[Depends(JWTBearer())])
def create_usuarios(usuario: Usuarios):
    db = Session()
    usuarios = UsuariosServices(db).create_usuarios(usuario)
    if not usuarios:
        return JSONResponse(status_code=500, content={"message": "Usuario no creado"})
    return JSONResponse(status_code=200, content={"message": "Usuario creado con exito"})

@usuarios_router.put('/USUARIOS', tags=['Usuarios'], response_model=Usuarios, status_code=200, dependencies=[Depends(JWTBearer())])
def update_usuarios(id: int, usuario: Usuarios):
    db = Session()
    usuarios = UsuariosServices(db).update_usuarios(id, usuario)
    if not usuarios:
        return JSONResponse(status_code=200, content={"message": "Usuario modificado con exito"})
    return JSONResponse(status_code=500, content={"message": "Usuario no modificado"})


@usuarios_router.delete('/USUARIOS', tags=['Usuarios'], response_model=Usuarios, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_usuarios(id: int):
    db = Session()
    usuarios = UsuariosServices(db).delete_usuarios(id)
    if not usuarios:
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado con exito"})
    return JSONResponse(status_code=500, content={"message": "Usuario no eliminado"})

