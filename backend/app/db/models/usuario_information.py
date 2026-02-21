from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Numeric
from datetime import datetime
from app.db.database import Base


class UsuarioInformation(Base):
    """Información personal detallada del usuario"""

    __tablename__ = "usuario_information"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False, index=True)
    es_conviviente = Column(Boolean, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    trabaja = Column(Boolean, nullable=True)
    ingresos_mensuales = Column(Numeric(10, 2), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    correo_personal = Column(String(255), nullable=True)
    correo_laboral = Column(String(255), nullable=True)
    tipo_via = Column(String(100), nullable=True)
    nombre_via = Column(String(255), nullable=True)
    numero_vivienda = Column(String(50), nullable=True)
    urbanizacion = Column(String(255), nullable=True)
    estado_civil = Column(String(50), nullable=True)
    distrito = Column(String(100), nullable=True)
    tipo_trabajo = Column(String(500), nullable=True)
    lugar_nacimiento = Column(String(100), nullable=True)
    sexo = Column(String(20), nullable=True)
    telefono_celular = Column(String(20), nullable=True)
