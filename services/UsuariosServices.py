from models.Usuarios import Usuarios as UsuariosModel
from schemas.UsuariosSchemas import Usuarios
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UsuariosServices():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_usuarios(self):
        usuarios = self.db.query(UsuariosModel).all()
        return usuarios
    
    def get_id_usuarios(self, id: int):
        usuarios = self.db.query(UsuariosModel).filter(UsuariosModel.id == id).first()
        return usuarios
    
    def get_email_usuarios(self, email: str):
        usuarios = self.db.query(UsuariosModel).filter(UsuariosModel.email == email).first()
        return usuarios
    
    def create_usuarios(self, usuario: Usuarios):
        contrasenia_hasheada = pwd_context.hash(usuario.password)
        usuario.password = contrasenia_hasheada
        new_usuario = UsuariosModel(**usuario.dict())        
        self.db.add(new_usuario)
        self.db.commit()
        return new_usuario
    
    def update_usuarios(self, id: int, data: Usuarios):
        usuario = self.db.query(UsuariosModel).filter(UsuariosModel.id == id).first()
        usuario.id = data.id
        usuario.nombre = data.nombre
        usuario.email = data.email
        usuario.password = data.password
        usuario.rol = data.rol
        self.db.commit()
        return
    
    def delete_usuarios(self, id: int):
        self.db.query(UsuariosModel).filter(UsuariosModel.id == id).delete()
        self.db.commit()
        return
    