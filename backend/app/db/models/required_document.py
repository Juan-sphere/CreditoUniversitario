from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, BigInteger
from datetime import datetime
from app.db.database import Base


class RequiredDocument(Base):
    """Documentos de sustentación requeridos"""

    __tablename__ = "required_documents"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Tipo de documento
    tipo_documento = Column(String(150), nullable=False)
    
    # Metadata del archivo en Cloud Storage
    bucket_name = Column(String(150), nullable=False)
    object_name = Column(Text, nullable=False)  # ruta dentro del bucket
    nombre_original = Column(String(255), nullable=False)
    mime_type = Column(String(100), nullable=True)
    size_bytes = Column(BigInteger, nullable=True)
    
    # Control interno
    estado = Column(String(30), nullable=False, default="PENDIENTE")  # PENDIENTE, VALIDADO, OBSERVADO
    observaciones = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
