from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import Session
from fastapi.responses import JSONResponse
from schemas.UserSchema import UsuarioAuth
from services.UserAuthServices import UserAuthService
from passlib.context import CryptContext

userauth_router = APIRouter()

@userauth_router.post('/login', tags=['Auth'])
def login(usuario_a_loguear: UsuarioAuth):
    db = Session()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    authenticated_user = UserAuthService(db, pwd_context).verify_user_credentials(usuario_a_loguear.email, usuario_a_loguear.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Correo o contraseña inválidos")
    
    token: str = create_token(usuario_a_loguear.model_dump())
    return JSONResponse(status_code=200, content={"token": token})