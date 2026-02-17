from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioRegistro(BaseModel):
    email: EmailStr
    nombre: str
    contraseña: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    contraseña: str

class GoogleLoginRequest(BaseModel):
    credential: str

class UsuarioResponse(BaseModel):
    id: int
    email: str
    nombre: str
    email_verificado: bool
    
    class Config:
        from_attributes = True