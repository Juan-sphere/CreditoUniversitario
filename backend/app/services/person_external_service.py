from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, PersonExternalInformation
from app.schemas.person_external import PersonExternalInformationCreate, PersonExternalInformationUpdate
import logging

logger = logging.getLogger(__name__)


class PersonExternalService:
    """Servicio para gestionar información de personas externas"""

    @staticmethod
    def crear_persona(
        usuario: Usuario, datos: PersonExternalInformationCreate, db: Session
    ) -> dict:
        """Crea un nuevo registro de persona externa"""
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] Creando persona externa para usuario: {usuario.nombre}")

        persona = PersonExternalInformation(usuario_id=usuario.id, **datos.dict())
        db.add(persona)
        db.commit()
        db.refresh(persona)
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] ✓ Persona externa creada para usuario {usuario.nombre}")

        return {
            "success": True,
            "mensaje": "Información de persona externa guardada correctamente",
            "data": {
                "id": persona.id,
                "nombre": persona.nombre,
                "parentesco_relacion": persona.parentesco_relacion,
            }
        }

    @staticmethod
    def obtener_personas(usuario: Usuario, db: Session) -> dict:
        """Obtiene todas las personas externas del usuario"""
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] Obteniendo personas externas para usuario: {usuario.nombre}")

        personas = db.query(PersonExternalInformation).filter(
            PersonExternalInformation.usuario_id == usuario.id
        ).all()

        resultado = []
        for persona in personas:
            resultado.append({
                "id": persona.id,
                "apellido_paterno": persona.apellido_paterno,
                "apellido_materno": persona.apellido_materno,
                "nombre": persona.nombre,
                "segundo_nombre": persona.segundo_nombre,
                "parentesco_relacion": persona.parentesco_relacion,
                "edad": persona.edad,
                "trabaja": persona.trabaja,
                "tipo_trabajo": persona.tipo_trabajo,
                "grado_instruccion": persona.grado_instruccion,
                "profesion_oficio": persona.profesion_oficio,
            })

        logger.info(f"[PERSON-EXTERNAL-SERVICE] ✓ Se obtuvieron {len(resultado)} personas externas para usuario {usuario.nombre}")

        return {"data": resultado}

    @staticmethod
    def obtener_persona(usuario: Usuario, persona_id: int, db: Session) -> dict:
        """Obtiene una persona externa específica"""
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] Obteniendo persona externa {persona_id} para usuario: {usuario.nombre}")

        persona = db.query(PersonExternalInformation).filter(
            PersonExternalInformation.id == persona_id,
            PersonExternalInformation.usuario_id == usuario.id
        ).first()

        if not persona:
            raise HTTPException(status_code=404, detail="Persona externa no encontrada")

        resultado = {
            "id": persona.id,
            "apellido_paterno": persona.apellido_paterno,
            "apellido_materno": persona.apellido_materno,
            "nombre": persona.nombre,
            "segundo_nombre": persona.segundo_nombre,
            "parentesco_relacion": persona.parentesco_relacion,
            "edad": persona.edad,
            "trabaja": persona.trabaja,
            "tipo_trabajo": persona.tipo_trabajo,
            "grado_instruccion": persona.grado_instruccion,
            "profesion_oficio": persona.profesion_oficio,
        }

        logger.info(f"[PERSON-EXTERNAL-SERVICE] ✓ Persona externa {persona_id} obtenida")

        return {"data": resultado}

    @staticmethod
    def actualizar_persona(
        usuario: Usuario, persona_id: int, datos: PersonExternalInformationUpdate, db: Session
    ) -> dict:
        """Actualiza los datos de una persona externa"""
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] Actualizando persona externa {persona_id} para usuario: {usuario.nombre}")

        persona = db.query(PersonExternalInformation).filter(
            PersonExternalInformation.id == persona_id,
            PersonExternalInformation.usuario_id == usuario.id
        ).first()

        if not persona:
            raise HTTPException(status_code=404, detail="Persona externa no encontrada")

        datos_dict = datos.dict(exclude_unset=True)
        for campo, valor in datos_dict.items():
            setattr(persona, campo, valor)

        db.commit()
        db.refresh(persona)

        logger.info(f"[PERSON-EXTERNAL-SERVICE] ✓ Persona externa {persona_id} actualizada")

        return {
            "success": True,
            "mensaje": "Persona externa actualizada correctamente",
            "data": {
                "id": persona.id,
                "nombre": persona.nombre,
            }
        }

    @staticmethod
    def eliminar_persona(usuario: Usuario, persona_id: int, db: Session) -> dict:
        """Elimina una persona externa"""
        
        logger.info(f"[PERSON-EXTERNAL-SERVICE] Eliminando persona externa {persona_id} para usuario: {usuario.nombre}")

        persona = db.query(PersonExternalInformation).filter(
            PersonExternalInformation.id == persona_id,
            PersonExternalInformation.usuario_id == usuario.id
        ).first()

        if not persona:
            raise HTTPException(status_code=404, detail="Persona externa no encontrada")

        db.delete(persona)
        db.commit()

        logger.info(f"[PERSON-EXTERNAL-SERVICE] ✓ Persona externa {persona_id} eliminada")

        return {
            "success": True,
            "mensaje": "Persona externa eliminada correctamente",
        }
