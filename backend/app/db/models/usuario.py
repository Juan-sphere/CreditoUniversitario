from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.database import Base


class Usuario(Base):
    """Usuarios registrados en el sistema"""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    universidad = Column(String(255), nullable=False)
    codigo_universidad = Column(String(20), unique=True, nullable=True, index=True)
    numero_documento = Column(String(20), unique=True, nullable=False, index=True)
    tipo_documento = Column(String(10), nullable=False)
    nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    correo_universidad = Column(String(255), nullable=False)
    contraseña_hash = Column(String(255), nullable=False)
    email_verificado = Column(Boolean, default=False)
    token_verificacion = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
