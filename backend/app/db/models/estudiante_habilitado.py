from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from app.db.database import Base


class EstudianteHabilitado(Base):
    """Estudiantes autorizados por la universidad para registrarse"""

    __tablename__ = "estudiantes_habilitados"

    id = Column(Integer, primary_key=True, index=True)
    universidad = Column(String(255), nullable=False, index=True)
    tipo_documento = Column(String(10), nullable=False)
    numero_documento = Column(String(20), unique=True, nullable=False, index=True)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    correo_universidad = Column(String(255), nullable=False)
    fecha_inicio_habilitacion = Column(Date, nullable=False)
    fecha_fin_habilitacion = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
