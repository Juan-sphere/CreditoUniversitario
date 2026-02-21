from pydantic import BaseModel
from typing import Optional
from datetime import date


class FamilyInformationCreate(BaseModel):
    """Schema para crear información de familiar"""
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str] = None
    parentesco: str
    depende_economicamente: bool
    edad: int
    estudia: bool
    trabaja: bool
    tipo_trabajo: Optional[str] = None
    tiene_empresa: bool = False
    contribuye_economia: bool
    grado_instruccion: str
    profesion_oficio: Optional[str] = None
    problemas_salud: bool

    class Config:
        from_attributes = True


class FamilyInformationUpdate(BaseModel):
    """Schema para actualizar información de familiar"""
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    nombre: Optional[str] = None
    segundo_nombre: Optional[str] = None
    parentesco: Optional[str] = None
    depende_economicamente: Optional[bool] = None
    edad: Optional[int] = None
    estudia: Optional[bool] = None
    trabaja: Optional[bool] = None
    tipo_trabajo: Optional[str] = None
    tiene_empresa: Optional[bool] = None
    contribuye_economia: Optional[bool] = None
    grado_instruccion: Optional[str] = None
    profesion_oficio: Optional[str] = None
    problemas_salud: Optional[bool] = None

    class Config:
        from_attributes = True


class FamilyInformationResponse(BaseModel):
    """Schema para respuesta de información de familiar"""
    id: int
    usuario_id: int
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str] = None
    parentesco: str
    depende_economicamente: bool
    edad: int
    estudia: bool
    trabaja: bool
    tipo_trabajo: Optional[str] = None
    tiene_empresa: bool
    contribuye_economia: bool
    grado_instruccion: str
    profesion_oficio: Optional[str] = None
    problemas_salud: bool

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True
