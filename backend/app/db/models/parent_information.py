from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Enum as SQLEnum, ForeignKey
from datetime import datetime
from app.db.database import Base
import enum


class ParentTypeEnum(str, enum.Enum):
    """Tipo de progenitor"""
    PADRE = "PADRE"
    MADRE = "MADRE"


class DocumentTypeEnum(str, enum.Enum):
    """Tipo de documento"""
    DNI = "DNI"
    CE = "CE"
    PASAPORTE = "PASAPORTE"


class ParentInformation(Base):
    """Información de los progenitores del usuario"""

    __tablename__ = "parents_information"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Tipo de progenitor
    parent_type = Column(SQLEnum(ParentTypeEnum), nullable=False)
    
    # Datos generales
    tipo_documento = Column(String(20), nullable=False)
    numero_documento = Column(String(20), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    fecha_nacimiento = Column(Date, nullable=False)
    vive = Column(Boolean, nullable=False)
    estado_civil = Column(String(50), nullable=False)
    es_conviviente = Column(Boolean, nullable=False)
    
    # Datos de contacto
    correo_personal = Column(String(255), nullable=True)
    correo_trabajo = Column(String(255), nullable=True)
    telefono_celular = Column(String(20), nullable=True)
    celular_trabajo = Column(String(20), nullable=True)
    
    # Datos laborales
    vive_con_usuario = Column(Boolean, nullable=False)
    trabaja = Column(Boolean, nullable=False)
    tipo_trabajo = Column(String(100), nullable=True)
    tiene_empresa = Column(Boolean, nullable=True)
    responsable_economia = Column(Boolean, nullable=True)
    contribuye_economia = Column(Boolean, nullable=True)
    grado_instruccion = Column(String(100), nullable=True)
    profesion_oficio = Column(String(150), nullable=True)
    problemas_salud = Column(Boolean, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
