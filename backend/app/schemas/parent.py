from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum


class ParentTypeEnum(str, Enum):
    """Tipo de progenitor"""
    PADRE = "PADRE"
    MADRE = "MADRE"


class DocumentTypeEnum(str, Enum):
    """Tipo de documento"""
    DNI = "DNI"
    CE = "CE"
    PASAPORTE = "PASAPORTE"


class ParentInformationCreate(BaseModel):
    """Schema para crear información de progenitor"""
    parent_type: ParentTypeEnum
    
    # Datos generales
    tipo_documento: str
    numero_documento: str
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str] = None
    fecha_nacimiento: date
    vive: bool
    estado_civil: str
    es_conviviente: bool
    
    # Datos de contacto
    correo_personal: Optional[str] = None
    correo_trabajo: Optional[str] = None
    telefono_celular: Optional[str] = None
    celular_trabajo: Optional[str] = None
    
    # Datos laborales
    vive_con_usuario: bool
    trabaja: bool
    tipo_trabajo: Optional[str] = None
    tiene_empresa: Optional[bool] = None
    responsable_economia: Optional[bool] = None
    contribuye_economia: Optional[bool] = None
    grado_instruccion: Optional[str] = None
    profesion_oficio: Optional[str] = None
    problemas_salud: bool


class ParentInformationUpdate(BaseModel):
    """Schema para actualizar información de progenitor"""
    # Datos generales
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    nombre: Optional[str] = None
    segundo_nombre: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    vive: Optional[bool] = None
    estado_civil: Optional[str] = None
    es_conviviente: Optional[bool] = None
    
    # Datos de contacto
    correo_personal: Optional[str] = None
    correo_trabajo: Optional[str] = None
    telefono_celular: Optional[str] = None
    celular_trabajo: Optional[str] = None
    
    # Datos laborales
    vive_con_usuario: Optional[bool] = None
    trabaja: Optional[bool] = None
    tipo_trabajo: Optional[str] = None
    tiene_empresa: Optional[bool] = None
    responsable_economia: Optional[bool] = None
    contribuye_economia: Optional[bool] = None
    grado_instruccion: Optional[str] = None
    profesion_oficio: Optional[str] = None
    problemas_salud: Optional[bool] = None


class ParentInformationResponse(BaseModel):
    """Schema para respuesta de información de progenitor"""
    id: int
    usuario_id: int
    parent_type: ParentTypeEnum
    
    # Datos generales
    tipo_documento: str
    numero_documento: str
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str]
    fecha_nacimiento: date
    vive: bool
    estado_civil: str
    es_conviviente: bool
    
    # Datos de contacto
    correo_personal: Optional[str]
    correo_trabajo: Optional[str]
    telefono_celular: Optional[str]
    celular_trabajo: Optional[str]
    
    # Datos laborales
    vive_con_usuario: bool
    trabaja: bool
    tipo_trabajo: Optional[str]
    tiene_empresa: Optional[bool]
    responsable_economia: Optional[bool]
    contribuye_economia: Optional[bool]
    grado_instruccion: Optional[str]
    profesion_oficio: Optional[str]
    problemas_salud: bool
    
    class Config:
        from_attributes = True
