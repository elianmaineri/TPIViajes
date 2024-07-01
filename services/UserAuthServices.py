from models.Usuarios import Usuarios as UsuariosModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext


class UserAuthService:
    def __init__(self, db: Session, pwd_context: CryptContext):
        self.db = db
        self.pwd_context = pwd_context

    def verify_user_credentials(self, email: str, password: str) -> UsuariosModel:
        user = self.db.query(UsuariosModel).filter(UsuariosModel.email == email).first()
        if user and self.pwd_context.verify(password, user.password):
            return user
        return None
