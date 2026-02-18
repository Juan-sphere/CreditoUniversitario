from pydantic import BaseModel, EmailStr
from datetime import datetime, date

# ==================== ESTUDIANTE HABILITADO ====================
class EstudianteHabilitadoCreate(BaseModel):
    codigo_universidad: str
    tipo_documento: str  # "DNI" o "CE"
    numero_documento: str
    nombres: str
    apellido_paterno: str
    apellido_materno: str
    correo_universidad: EmailStr
    fecha_inicio_habilitacion: date
    fecha_fin_habilitacion: date

# ==================== REGISTRO ====================
class UsuarioRegistro(BaseModel):
    """
    Registro con DNI o Código de Universidad
    Solo puede registrarse si está en EstudiantesHabilitados
    """
    identificador: str  # DNI o Código de Universidad
    contraseña: str
    confirmar_contraseña: str

# ==================== LOGIN ====================
class UsuarioLogin(BaseModel):
    """
    Login con DNI (DNI99999999) o Código (codigo)
    """
    identificador: str  # DNI99999999 o CE888888888 o código
    contraseña: str

# ==================== RESPONSE ====================
class UsuarioResponse(BaseModel):
    id: int
    codigo_universidad: str
    numero_documento: str
    nombres: str
    apellido_paterno: str
    apellido_materno: str
    email_verificado: bool
    
    class Config:
        from_attributes = True