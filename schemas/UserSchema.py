from pydantic import BaseModel, EmailStr

class UsuarioAuth(BaseModel):
    email: EmailStr
    password: str