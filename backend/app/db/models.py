from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    google_id = Column(String(255), unique=True, index=True, nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    contraseña_hash = Column(String(255), nullable=True)  
    email_verificado = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    creditos = relationship("Creditos", back_populates="usuario", cascade="all, delete-orphan")
    inscripciones = relationship("Inscripcion", back_populates="usuario", cascade="all, delete-orphan")

class Creditos(Base):
    __tablename__ = "creditos"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    creditos_totales = Column(Integer, default=120)
    creditos_cursados = Column(Integer, default=0)
    creditos_disponibles = Column(Integer, default=120)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relación
    usuario = relationship("Usuario", back_populates="creditos")

class Materia(Base):
    __tablename__ = "materias"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    creditos = Column(Integer, nullable=False)
    semestre = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relación
    inscripciones = relationship("Inscripcion", back_populates="materia", cascade="all, delete-orphan")

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)
    fecha_inscripcion = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(50), default="inscrito")
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="inscripciones")
    materia = relationship("Materia", back_populates="inscripciones")