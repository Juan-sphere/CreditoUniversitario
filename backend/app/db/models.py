from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from datetime import datetime
from app.db.database import Base

class EstudianteHabilitado(Base):
    """Estudiantes que pueden registrarse"""
    __tablename__ = "estudiantes_habilitados"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo_universidad = Column(String(20), unique=True, nullable=False, index=True)
    tipo_documento = Column(String(10), nullable=False)
    numero_documento = Column(String(20), unique=True, nullable=False, index=True)
    nombres = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    correo_universidad = Column(String(255), nullable=False)
    fecha_inicio_habilitacion = Column(Date, nullable=False)
    fecha_fin_habilitacion = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Usuario(Base):
    """Usuarios registrados"""
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo_universidad = Column(String(20), unique=True, nullable=False, index=True)
    numero_documento = Column(String(20), unique=True, nullable=False, index=True)
    tipo_documento = Column(String(10), nullable=False)
    nombres = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    correo_universidad = Column(String(255), nullable=False)
    contraseña_hash = Column(String(255), nullable=False)
    email_verificado = Column(Boolean, default=False)
    token_verificacion = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)