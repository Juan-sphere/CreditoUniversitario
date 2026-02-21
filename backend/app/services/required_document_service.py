from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, RequiredDocument
from app.schemas.required_document import RequiredDocumentCreate, RequiredDocumentUpdate
import logging

logger = logging.getLogger(__name__)


class RequiredDocumentService:
    """Servicio para gestionar documentos requeridos"""

    @staticmethod
    def crear_documento(
        usuario: Usuario, datos: RequiredDocumentCreate, db: Session
    ) -> dict:
        """Crea un nuevo registro de documento"""
        
        logger.info(f"[DOCUMENT-SERVICE] Creando documento para usuario: {usuario.nombre}")

        documento = RequiredDocument(usuario_id=usuario.id, **datos.dict())
        db.add(documento)
        db.commit()
        db.refresh(documento)
        
        logger.info(f"[DOCUMENT-SERVICE] ✓ Documento creado para usuario {usuario.nombre}")

        return {
            "success": True,
            "mensaje": "Documento guardado correctamente",
            "data": {
                "id": documento.id,
                "tipo_documento": documento.tipo_documento,
                "nombre_original": documento.nombre_original,
                "object_name": documento.object_name,
            }
        }

    @staticmethod
    def obtener_documentos(usuario: Usuario, db: Session) -> dict:
        """Obtiene todos los documentos del usuario"""
        
        logger.info(f"[DOCUMENT-SERVICE] Obteniendo documentos para usuario: {usuario.nombre}")

        documentos = db.query(RequiredDocument).filter(
            RequiredDocument.usuario_id == usuario.id
        ).all()

        resultado = []
        for doc in documentos:
            resultado.append({
                "id": doc.id,
                "tipo_documento": doc.tipo_documento,
                "bucket_name": doc.bucket_name,
                "object_name": doc.object_name,
                "nombre_original": doc.nombre_original,
                "mime_type": doc.mime_type,
                "size_bytes": doc.size_bytes,
                "estado": doc.estado,
                "observaciones": doc.observaciones,
                "created_at": doc.created_at,
                "updated_at": doc.updated_at,
            })

        logger.info(f"[DOCUMENT-SERVICE] ✓ Se obtuvieron {len(resultado)} documentos para usuario {usuario.nombre}")

        return {"data": resultado}

    @staticmethod
    def obtener_documento(usuario: Usuario, documento_id: int, db: Session) -> dict:
        """Obtiene un documento específico"""
        
        logger.info(f"[DOCUMENT-SERVICE] Obteniendo documento {documento_id} para usuario: {usuario.nombre}")

        documento = db.query(RequiredDocument).filter(
            RequiredDocument.id == documento_id,
            RequiredDocument.usuario_id == usuario.id
        ).first()

        if not documento:
            raise HTTPException(status_code=404, detail="Documento no encontrado")

        resultado = {
            "id": documento.id,
            "tipo_documento": documento.tipo_documento,
            "bucket_name": documento.bucket_name,
            "object_name": documento.object_name,
            "nombre_original": documento.nombre_original,
            "mime_type": documento.mime_type,
            "size_bytes": documento.size_bytes,
            "estado": documento.estado,
            "observaciones": documento.observaciones,
            "created_at": documento.created_at,
            "updated_at": documento.updated_at,
        }

        logger.info(f"[DOCUMENT-SERVICE] ✓ Documento {documento_id} obtenido")

        return {"data": resultado}

    @staticmethod
    def obtener_documentos_por_tipo(usuario: Usuario, tipo: str, db: Session) -> dict:
        """Obtiene documentos filtrados por tipo"""
        
        logger.info(f"[DOCUMENT-SERVICE] Obteniendo documentos tipo {tipo} para usuario: {usuario.nombre}")

        documentos = db.query(RequiredDocument).filter(
            RequiredDocument.usuario_id == usuario.id,
            RequiredDocument.tipo_documento == tipo
        ).all()

        resultado = [
            {
                "id": doc.id,
                "tipo_documento": doc.tipo_documento,
                "bucket_name": doc.bucket_name,
                "object_name": doc.object_name,
                "nombre_original": doc.nombre_original,
                "estado": doc.estado,
                "created_at": doc.created_at,
            }
            for doc in documentos
        ]

        logger.info(f"[DOCUMENT-SERVICE] ✓ Se obtuvieron {len(resultado)} documentos tipo {tipo}")

        return {"data": resultado}

    @staticmethod
    def actualizar_documento(
        usuario: Usuario, documento_id: int, datos: RequiredDocumentUpdate, db: Session
    ) -> dict:
        """Actualiza los datos de un documento"""
        
        logger.info(f"[DOCUMENT-SERVICE] Actualizando documento {documento_id} para usuario: {usuario.nombre}")

        documento = db.query(RequiredDocument).filter(
            RequiredDocument.id == documento_id,
            RequiredDocument.usuario_id == usuario.id
        ).first()

        if not documento:
            raise HTTPException(status_code=404, detail="Documento no encontrado")

        datos_dict = datos.dict(exclude_unset=True)
        for campo, valor in datos_dict.items():
            setattr(documento, campo, valor)

        db.commit()
        db.refresh(documento)

        logger.info(f"[DOCUMENT-SERVICE] ✓ Documento {documento_id} actualizado")

        return {
            "success": True,
            "mensaje": "Documento actualizado correctamente",
            "data": {
                "id": documento.id,
                "estado": documento.estado,
            }
        }

    @staticmethod
    def eliminar_documento(usuario: Usuario, documento_id: int, db: Session) -> dict:
        """Elimina un documento"""
        
        logger.info(f"[DOCUMENT-SERVICE] Eliminando documento {documento_id} para usuario: {usuario.nombre}")

        documento = db.query(RequiredDocument).filter(
            RequiredDocument.id == documento_id,
            RequiredDocument.usuario_id == usuario.id
        ).first()

        if not documento:
            raise HTTPException(status_code=404, detail="Documento no encontrado")

        db.delete(documento)
        db.commit()

        logger.info(f"[DOCUMENT-SERVICE] ✓ Documento {documento_id} eliminado")

        return {
            "success": True,
            "mensaje": "Documento eliminado correctamente",
        }
