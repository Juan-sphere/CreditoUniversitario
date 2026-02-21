from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import EstudianteHabilitado
import logging

logger = logging.getLogger(__name__)


class EstudianteService:
    """Servicio para gestionar estudiantes habilitados"""

    @staticmethod
    def listar_universidades(db: Session) -> list:
        """Obtiene lista de universidades disponibles"""
        logger.info("[ESTUDIANTE-SERVICE] Obteniendo universidades")
        universidades = db.query(EstudianteHabilitado.universidad).distinct().all()
        return [u[0] for u in universidades]

    @staticmethod
    def buscar_estudiante_por_dni(dni: str, db: Session) -> dict:
        """Busca estudiante habilitado por DNI"""
        logger.info(f"[ESTUDIANTE-SERVICE] Buscando estudiante con DNI: {dni[:3]}***")

        # Limpiar DNI
        dni_limpio = dni.strip().upper()
        if dni_limpio.startswith("DNI"):
            dni_limpio = dni_limpio[3:]
        if dni_limpio.startswith("CE"):
            dni_limpio = dni_limpio[2:]

        # Buscar estudiante
        estudiante = (
            db.query(EstudianteHabilitado)
            .filter(EstudianteHabilitado.numero_documento == dni_limpio)
            .first()
        )

        if not estudiante:
            logger.warning(f"[ESTUDIANTE-SERVICE] DNI no encontrado: {dni_limpio[:3]}***")
            raise HTTPException(status_code=404, detail="DNI no encontrado")

        # Verificar fechas
        hoy = date.today()
        if not (
            estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion
        ):
            logger.warning(f"[ESTUDIANTE-SERVICE] Habilitación expirada para DNI: {dni_limpio[:3]}***")
            raise HTTPException(status_code=403, detail="Tu habilitación ha expirado")

        logger.info(f"[ESTUDIANTE-SERVICE] ✓ Estudiante encontrado: {estudiante.nombre}")

        return {
            "universidad": estudiante.universidad,
            "correo_universidad": estudiante.correo_universidad,
            "nombre": estudiante.nombre,
            "segundo_nombre": estudiante.segundo_nombre,
            "apellido_paterno": estudiante.apellido_paterno,
            "apellido_materno": estudiante.apellido_materno,
        }
