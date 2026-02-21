from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base


class PersonExternalInformation(Base):
    """Información de personas externas que contribuyen a la economía familiar"""

    __tablename__ = "person_external_information"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Datos generales
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    
    # Relación
    parentesco_relacion = Column(String(150), nullable=False)
    
    # Información laboral
    edad = Column(Integer, nullable=False)
    trabaja = Column(Boolean, nullable=False)
    tipo_trabajo = Column(String(150), nullable=True)
    
    # Datos laborales y académicos
    grado_instruccion = Column(String(150), nullable=False)
    profesion_oficio = Column(String(150), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
