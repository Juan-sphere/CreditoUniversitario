from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RequiredDocumentCreate(BaseModel):
    """Schema para crear documento requerido"""
    tipo_documento: str
    bucket_name: str = "credito-universitario-docs-2026"
    object_name: str
    nombre_original: str
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None

    class Config:
        from_attributes = True


class RequiredDocumentUpdate(BaseModel):
    """Schema para actualizar documento"""
    estado: Optional[str] = None
    observaciones: Optional[str] = None

    class Config:
        from_attributes = True


class RequiredDocumentResponse(BaseModel):
    """Schema para respuesta de documento"""
    id: int
    usuario_id: int
    tipo_documento: str
    bucket_name: str
    object_name: str
    nombre_original: str
    mime_type: Optional[str] = None
    size_bytes: Optional[int] = None
    estado: str
    observaciones: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RequiredDocumentUploadResponse(BaseModel):
    """Schema para respuesta de carga de documento"""
    success: bool
    mensaje: str
    document_id: int
    object_name: str
    tipo_documento: str
