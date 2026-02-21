from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, ParentInformation
from app.schemas.parent import ParentInformationCreate, ParentInformationUpdate, ParentTypeEnum
import logging

logger = logging.getLogger(__name__)


class ParentService:
    """Servicio para gestionar información de progenitores"""

    @staticmethod
    def guardar_or_actualizar_padre(
        usuario: Usuario, datos: ParentInformationCreate, db: Session
    ) -> dict:
        """Guarda o actualiza la información de un progenitor"""
        
        logger.info(f"[PARENT-SERVICE] Guardando información de {datos.parent_type.value} para usuario: {usuario.nombre}")

        # Buscar si ya existe registro de este progenitor
        parent = db.query(ParentInformation).filter(
            ParentInformation.usuario_id == usuario.id,
            ParentInformation.parent_type == datos.parent_type
        ).first()

        if parent:
            # Actualizar
            logger.info(f"[PARENT-SERVICE] Actualizando {datos.parent_type.value}")
            for campo, valor in datos.dict(exclude_none=True).items():
                if campo != 'parent_type':  # No cambiar el tipo
                    setattr(parent, campo, valor)
        else:
            # Crear
            logger.info(f"[PARENT-SERVICE] Creando nuevo registro de {datos.parent_type.value}")
            parent = ParentInformation(usuario_id=usuario.id, **datos.dict())
            db.add(parent)

        db.commit()
        db.refresh(parent)
        
        logger.info(f"[PARENT-SERVICE] ✓ Información de {datos.parent_type.value} guardada para usuario {usuario.nombre}")

        return {
            "success": True,
            "mensaje": f"Información del {datos.parent_type.value.lower()} guardada correctamente",
            "data": {
                "id": parent.id,
                "parent_type": parent.parent_type.value,
                "nombre": parent.nombre,
                "apellido_paterno": parent.apellido_paterno,
            }
        }

    @staticmethod
    def obtener_padres(usuario: Usuario, db: Session) -> dict:
        """Obtiene la información de ambos progenitores del usuario"""
        
        logger.info(f"[PARENT-SERVICE] Obteniendo información de padres para usuario: {usuario.nombre}")

        padres = db.query(ParentInformation).filter(
            ParentInformation.usuario_id == usuario.id
        ).all()

        resultado = {}
        for padre in padres:
            resultado[padre.parent_type.value.lower()] = {
                "id": padre.id,
                "parent_type": padre.parent_type.value,
                "tipo_documento": padre.tipo_documento,
                "numero_documento": padre.numero_documento,
                "apellido_paterno": padre.apellido_paterno,
                "apellido_materno": padre.apellido_materno,
                "nombre": padre.nombre,
                "segundo_nombre": padre.segundo_nombre,
                "fecha_nacimiento": str(padre.fecha_nacimiento) if padre.fecha_nacimiento else None,
                "vive": padre.vive,
                "estado_civil": padre.estado_civil,
                "es_conviviente": padre.es_conviviente,
                "correo_personal": padre.correo_personal,
                "correo_trabajo": padre.correo_trabajo,
                "telefono_celular": padre.telefono_celular,
                "celular_trabajo": padre.celular_trabajo,
                "vive_con_usuario": padre.vive_con_usuario,
                "trabaja": padre.trabaja,
                "tipo_trabajo": padre.tipo_trabajo,
                "tiene_empresa": padre.tiene_empresa,
                "responsable_economia": padre.responsable_economia,
                "contribuye_economia": padre.contribuye_economia,
                "grado_instruccion": padre.grado_instruccion,
                "profesion_oficio": padre.profesion_oficio,
                "problemas_salud": padre.problemas_salud,
            }

        logger.info(f"[PARENT-SERVICE] ✓ Información de padres obtenida para usuario {usuario.nombre}")

        return {"data": resultado}

    @staticmethod
    def eliminar_padre(usuario: Usuario, parent_type: ParentTypeEnum, db: Session) -> dict:
        """Elimina la información de un progenitor"""
        
        logger.info(f"[PARENT-SERVICE] Eliminando información de {parent_type.value} para usuario: {usuario.nombre}")

        parent = db.query(ParentInformation).filter(
            ParentInformation.usuario_id == usuario.id,
            ParentInformation.parent_type == parent_type
        ).first()

        if not parent:
            raise HTTPException(status_code=404, detail=f"{parent_type.value} no encontrado")

        db.delete(parent)
        db.commit()
        
        logger.info(f"[PARENT-SERVICE] ✓ Información de {parent_type.value} eliminada para usuario {usuario.nombre}")

        return {
            "success": True,
            "mensaje": f"Información del {parent_type.value.lower()} eliminada correctamente"
        }
