from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base


class FamilyInformation(Base):
    """Información de familiares del usuario"""

    __tablename__ = "family_information"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Datos generales
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    
    # Relación
    parentesco = Column(String(100), nullable=False)
    
    # Información socioeconómica
    depende_economicamente = Column(Boolean, nullable=False)
    edad = Column(Integer, nullable=False)
    estudia = Column(Boolean, nullable=False)
    trabaja = Column(Boolean, nullable=False)
    tipo_trabajo = Column(String(100), nullable=True)
    tiene_empresa = Column(Boolean, nullable=False, default=False)
    
    # Datos laborales y académicos
    contribuye_economia = Column(Boolean, nullable=False)
    grado_instruccion = Column(String(100), nullable=False)
    profesion_oficio = Column(String(150), nullable=True)
    problemas_salud = Column(Boolean, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
