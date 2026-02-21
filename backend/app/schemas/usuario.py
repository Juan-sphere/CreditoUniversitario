from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UsuarioRegistro(BaseModel):
    universidad: str
    dni: str
    correo_universidad: EmailStr
    contraseña: str
    confirmar_contraseña: str

class UsuarioLogin(BaseModel):
    dni: str
    contraseña: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

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


class InformacionPersonalUpdate(BaseModel):
    # Tab 0: Información adicional
    estado_civil: Optional[str] = None
    es_conviviente: Optional[bool] = None
    fecha_nacimiento: Optional[date] = None
    lugar_nacimiento: Optional[str] = None
    sexo: Optional[str] = None
    telefono_celular: Optional[str] = None
    # Tab 1: Correo
    correo_personal: Optional[str] = None
    correo_laboral: Optional[str] = None
    # Tab 2: Dirección
    tipo_via: Optional[str] = None
    nombre_via: Optional[str] = None
    numero_vivienda: Optional[str] = None
    urbanizacion: Optional[str] = None
    distrito: Optional[str] = None
    # Tab 3: Datos laborales
    trabaja: Optional[bool] = None
    tipo_trabajo: Optional[str] = None
    ingresos_mensuales: Optional[float] = None