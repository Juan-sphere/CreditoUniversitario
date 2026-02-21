from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, FamilyInformation
from app.schemas.family import FamilyInformationCreate, FamilyInformationUpdate
import logging

logger = logging.getLogger(__name__)


class FamilyService:
    """Servicio para gestionar información de familiares"""

    @staticmethod
    def crear_familiar(
        usuario: Usuario, datos: FamilyInformationCreate, db: Session
    ) -> dict:
        """Crea un nuevo registro de familiar"""
        
        logger.info(f"[FAMILY-SERVICE] Creando registro de familiar para usuario: {usuario.nombre}")

        familiar = FamilyInformation(usuario_id=usuario.id, **datos.dict())
        db.add(familiar)
        db.commit()
        db.refresh(familiar)
        
        logger.info(f"[FAMILY-SERVICE] ✓ Familiar creado para usuario {usuario.nombre}")

        return {
            "success": True,
            "mensaje": "Información de familiar guardada correctamente",
            "data": {
                "id": familiar.id,
                "nombre": familiar.nombre,
                "parentesco": familiar.parentesco,
            }
        }

    @staticmethod
    def obtener_familiares(usuario: Usuario, db: Session) -> dict:
        """Obtiene todos los familiares del usuario"""
        
        logger.info(f"[FAMILY-SERVICE] Obteniendo familiares para usuario: {usuario.nombre}")

        familiares = db.query(FamilyInformation).filter(
            FamilyInformation.usuario_id == usuario.id
        ).all()

        resultado = []
        for familiar in familiares:
            resultado.append({
                "id": familiar.id,
                "apellido_paterno": familiar.apellido_paterno,
                "apellido_materno": familiar.apellido_materno,
                "nombre": familiar.nombre,
                "segundo_nombre": familiar.segundo_nombre,
                "parentesco": familiar.parentesco,
                "depende_economicamente": familiar.depende_economicamente,
                "edad": familiar.edad,
                "estudia": familiar.estudia,
                "trabaja": familiar.trabaja,
                "tipo_trabajo": familiar.tipo_trabajo,
                "tiene_empresa": familiar.tiene_empresa,
                "contribuye_economia": familiar.contribuye_economia,
                "grado_instruccion": familiar.grado_instruccion,
                "profesion_oficio": familiar.profesion_oficio,
                "problemas_salud": familiar.problemas_salud,
            })

        logger.info(f"[FAMILY-SERVICE] ✓ Se obtuvieron {len(resultado)} familiares para usuario {usuario.nombre}")

        return {"data": resultado}

    @staticmethod
    def obtener_familiar(usuario: Usuario, familiar_id: int, db: Session) -> dict:
        """Obtiene un familiar específico"""
        
        logger.info(f"[FAMILY-SERVICE] Obteniendo familiar {familiar_id} para usuario: {usuario.nombre}")

        familiar = db.query(FamilyInformation).filter(
            FamilyInformation.id == familiar_id,
            FamilyInformation.usuario_id == usuario.id
        ).first()

        if not familiar:
            raise HTTPException(status_code=404, detail="Familiar no encontrado")

        resultado = {
            "id": familiar.id,
            "apellido_paterno": familiar.apellido_paterno,
            "apellido_materno": familiar.apellido_materno,
            "nombre": familiar.nombre,
            "segundo_nombre": familiar.segundo_nombre,
            "parentesco": familiar.parentesco,
            "depende_economicamente": familiar.depende_economicamente,
            "edad": familiar.edad,
            "estudia": familiar.estudia,
            "trabaja": familiar.trabaja,
            "tipo_trabajo": familiar.tipo_trabajo,
            "tiene_empresa": familiar.tiene_empresa,
            "contribuye_economia": familiar.contribuye_economia,
            "grado_instruccion": familiar.grado_instruccion,
            "profesion_oficio": familiar.profesion_oficio,
            "problemas_salud": familiar.problemas_salud,
        }

        logger.info(f"[FAMILY-SERVICE] ✓ Familiar obtenido")

        return {"data": resultado}

    @staticmethod
    def actualizar_familiar(
        usuario: Usuario, familiar_id: int, datos: FamilyInformationUpdate, db: Session
    ) -> dict:
        """Actualiza la información de un familiar"""
        
        logger.info(f"[FAMILY-SERVICE] Actualizando familiar {familiar_id} para usuario: {usuario.nombre}")

        familiar = db.query(FamilyInformation).filter(
            FamilyInformation.id == familiar_id,
            FamilyInformation.usuario_id == usuario.id
        ).first()

        if not familiar:
            raise HTTPException(status_code=404, detail="Familiar no encontrado")

        for campo, valor in datos.dict(exclude_none=True).items():
            setattr(familiar, campo, valor)

        db.commit()
        db.refresh(familiar)
        
        logger.info(f"[FAMILY-SERVICE] ✓ Familiar actualizado")

        return {
            "success": True,
            "mensaje": "Información de familiar actualizada correctamente",
            "data": {
                "id": familiar.id,
                "nombre": familiar.nombre,
                "parentesco": familiar.parentesco,
            }
        }

    @staticmethod
    def eliminar_familiar(usuario: Usuario, familiar_id: int, db: Session) -> dict:
        """Elimina un familiar"""
        
        logger.info(f"[FAMILY-SERVICE] Eliminando familiar {familiar_id} para usuario: {usuario.nombre}")

        familiar = db.query(FamilyInformation).filter(
            FamilyInformation.id == familiar_id,
            FamilyInformation.usuario_id == usuario.id
        ).first()

        if not familiar:
            raise HTTPException(status_code=404, detail="Familiar no encontrado")

        db.delete(familiar)
        db.commit()
        
        logger.info(f"[FAMILY-SERVICE] ✓ Familiar eliminado")

        return {
            "success": True,
            "mensaje": "Familiar eliminado correctamente"
        }
