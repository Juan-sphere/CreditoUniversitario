from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, UsuarioInformation
from app.schemas.usuario import InformacionPersonalUpdate
import logging

logger = logging.getLogger(__name__)


class InformacionPersonalService:
    """Servicio para gestionar información personal del usuario"""

    @staticmethod
    def guardar_informacion_personal(
        usuario: Usuario, datos: InformacionPersonalUpdate, db: Session
    ) -> dict:
        """Guarda o actualiza la información personal del usuario"""
        
        logger.info(f"[INFO-PERSONAL-SERVICE] Guardando información para usuario: {usuario.nombre}")

        # Buscar o crear registro
        info = db.query(UsuarioInformation).filter(
            UsuarioInformation.usuario_id == usuario.id
        ).first()

        if not info:
            info = UsuarioInformation(usuario_id=usuario.id)
            db.add(info)
            logger.info(f"[INFO-PERSONAL-SERVICE] Nuevo registro creado")

        # Actualizar campos
        for campo, valor in datos.dict(exclude_none=True).items():
            setattr(info, campo, valor)

        # Si no trabaja, establecer valores por defecto
        if info.trabaja == False:
            info.tipo_trabajo = "No tiene"
            info.ingresos_mensuales = 0

        db.commit()
        logger.info(f"[INFO-PERSONAL-SERVICE] ✓ Información actualizada para usuario {usuario.nombre}")

        return {"success": True, "mensaje": "Información guardada correctamente"}

    @staticmethod
    def obtener_informacion_personal(usuario: Usuario, db: Session) -> dict:
        """Obtiene la información personal del usuario"""
        
        logger.info(f"[INFO-PERSONAL-SERVICE] Obteniendo información para usuario: {usuario.nombre}")

        info = db.query(UsuarioInformation).filter(
            UsuarioInformation.usuario_id == usuario.id
        ).first()

        if not info:
            return {"data": None}

        return {
            "data": {
                "estado_civil": info.estado_civil,
                "es_conviviente": info.es_conviviente,
                "fecha_nacimiento": str(info.fecha_nacimiento) if info.fecha_nacimiento else None,
                "lugar_nacimiento": info.lugar_nacimiento,
                "sexo": info.sexo,
                "telefono_celular": info.telefono_celular,
                "correo_personal": info.correo_personal,
                "correo_laboral": info.correo_laboral,
                "tipo_via": info.tipo_via,
                "nombre_via": info.nombre_via,
                "numero_vivienda": info.numero_vivienda,
                "urbanizacion": info.urbanizacion,
                "distrito": info.distrito,
                "trabaja": info.trabaja,
                "tipo_trabajo": info.tipo_trabajo,
                "ingresos_mensuales": float(info.ingresos_mensuales) if info.ingresos_mensuales else None,
            }
        }
