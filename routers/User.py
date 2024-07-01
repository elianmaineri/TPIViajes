from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.Usuarios import Usuarios as UsuariosModel
from services.UsuariosServices import UsuariosServices
from schemas.UserSchema import UsuarioAuth
from schemas.UsuariosSchemas import Usuarios
from passlib.context import CryptContext

user_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(users:dict, email: str, password: str)-> Usuarios:
    user = get_user(users, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    user = Usuarios.model_validate(user)
    return user

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(users:list, email: str):
    for item in users:
        if item.email == email:
            return item

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)    

@user_router.post('/login', tags=['auth'])
def login(user: UsuarioAuth):
    db = Session()
    usuariosDb:UsuariosModel= UsuariosServices(db).get_all_usuarios()
   
    usuario= authenticate_user(usuariosDb, user.email, user.password)
    if not user:
       return JSONResponse(status_code=401, content={'accesoOk': False,'token':''})  
    else:
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content={'accesoOk': True,'token':token, 'usuario': jsonable_encoder(usuario) })