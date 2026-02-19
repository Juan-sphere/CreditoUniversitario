from pydantic import BaseModel, EmailStr
from datetime import date

class UsuarioRegistro(BaseModel):
    universidad: str
    dni: str
    correo_universidad: EmailStr
    contraseña: str
    confirmar_contraseña: str

class UsuarioLogin(BaseModel):
    dni: str
    contraseña: str

class EstudianteHabilitadoCreate(BaseModel):
    universidad: str
    tipo_documento: str
    numero_documento: str
    apellido_paterno: str
    apellido_materno: str
    nombres: str
    segundo_nombre: str = None
    correo_universidad: str
    fecha_inicio_habilitacion: date
    fecha_fin_habilitacion: date

class UsuarioResponse(BaseModel):
    id: int
    universidad: str
    numero_documento: str
    nombres: str
    apellido_paterno: str
    apellido_materno: str
    
    class Config:
        from_attributes = True