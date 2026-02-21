from pydantic import BaseModel
from typing import Optional


class PersonExternalInformationCreate(BaseModel):
    """Schema para crear información de persona externa"""
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str] = None
    parentesco_relacion: str
    edad: int
    trabaja: bool
    tipo_trabajo: Optional[str] = None
    grado_instruccion: str
    profesion_oficio: Optional[str] = None

    class Config:
        from_attributes = True


class PersonExternalInformationUpdate(BaseModel):
    """Schema para actualizar información de persona externa"""
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    nombre: Optional[str] = None
    segundo_nombre: Optional[str] = None
    parentesco_relacion: Optional[str] = None
    edad: Optional[int] = None
    trabaja: Optional[bool] = None
    tipo_trabajo: Optional[str] = None
    grado_instruccion: Optional[str] = None
    profesion_oficio: Optional[str] = None

    class Config:
        from_attributes = True


class PersonExternalInformationResponse(BaseModel):
    """Schema para respuesta de información de persona externa"""
    id: int
    usuario_id: int
    apellido_paterno: str
    apellido_materno: str
    nombre: str
    segundo_nombre: Optional[str] = None
    parentesco_relacion: str
    edad: int
    trabaja: bool
    tipo_trabajo: Optional[str] = None
    grado_instruccion: str
    profesion_oficio: Optional[str] = None

    class Config:
        from_attributes = True
