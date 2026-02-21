from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from app.db.database import get_db
from app.schemas.usuario import (
    UsuarioRegistro,
    UsuarioLogin,
    InformacionPersonalUpdate,
)
from app.services.auth_service import AuthService
from app.services.informacion_personal_service import InformacionPersonalService
from app.services.estudiante_service import EstudianteService
from app.services.jwt_service import get_current_user
from app.utils.token import get_token_from_header
from app.db.models import Usuario
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


# ==================== REGISTRO ====================
@router.post("/registro")
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    """Registro de estudiante habilitado"""
    return AuthService.registrar_usuario(datos, db)


# ==================== LOGIN ====================
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """Login con DNI y generación de JWT token"""
    return AuthService.login_usuario(datos, db)


# ==================== OBTENER USUARIO ACTUAL ====================
@router.get("/me")
def obtener_usuario_actual(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Obtiene los datos del usuario autenticado"""
    logger.info("[AUTH] GET /me - Solicitud recibida")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[AUTH] ✓ Usuario obtenido: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[AUTH] ❌ Error: {str(e)}")
        raise

    return {
        "success": True,
        "usuario": {
            "id": usuario.id,
            "universidad": usuario.universidad,
            "numero_documento": usuario.numero_documento,
            "tipo_documento": usuario.tipo_documento,
            "nombre": usuario.nombre,
            "segundo_nombre": usuario.segundo_nombre,
            "apellido_paterno": usuario.apellido_paterno,
            "apellido_materno": usuario.apellido_materno,
            "correo_universidad": usuario.correo_universidad,
            "email_verificado": usuario.email_verificado,
        },
    }


# ==================== VERIFICAR TOKEN ====================
@router.get("/verificar")
def verificar_token_endpoint(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Verifica si el token es válido"""
    logger.info("[AUTH] GET /verificar - Verificando token")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[AUTH] ✓ Token válido para usuario: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[AUTH] ❌ Token inválido: {str(e)}")
        raise

    return {"success": True, "mensaje": "Token válido", "usuario_id": usuario.id}


# ==================== INFORMACIÓN PERSONAL ====================
@router.post("/informacion-personal")
def guardar_informacion_personal(
    datos: InformacionPersonalUpdate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Guarda o actualiza la información personal del usuario autenticado"""
    logger.info("[INFO-PERSONAL] Solicitud recibida para guardar información personal")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[INFO-PERSONAL] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[INFO-PERSONAL] ❌ Error de autenticación: {str(e)}")
        raise

    return InformacionPersonalService.guardar_informacion_personal(usuario, datos, db)


@router.get("/informacion-personal")
def obtener_informacion_personal(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Obtiene la información personal del usuario autenticado"""
    logger.info("[INFO-PERSONAL] Solicitud para obtener información personal")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[INFO-PERSONAL] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[INFO-PERSONAL] ❌ Error de autenticación: {str(e)}")
        raise

    return InformacionPersonalService.obtener_informacion_personal(usuario, db)


# ==================== OBTENER UNIVERSIDADES ====================
@router.get("/universidades")
def listar_universidades(db: Session = Depends(get_db)):
    """Obtener lista de universidades disponibles (sin requerir autenticación)"""
    logger.info("[UNIVERSIDADES] GET /universidades - Listando universidades")
    return EstudianteService.listar_universidades(db)


# ==================== BUSCAR ESTUDIANTE POR DNI ====================
@router.get("/buscar-estudiante/{dni}")
def buscar_estudiante(dni: str, db: Session = Depends(get_db)):
    """Buscar estudiante habilitado por DNI para autocompletar registro (sin autenticación)"""
    logger.info(f"[ESTUDIANTE] GET /buscar-estudiante/{dni[:3]}*** - Buscando estudiante")
    return EstudianteService.buscar_estudiante_por_dni(dni, db)


# ==================== DEBUG - LISTAR USUARIOS ====================
@router.get("/debug/usuarios")
def debug_listar_usuarios(db: Session = Depends(get_db)):
    """[DEBUG] Listar todos los usuarios registrados - SOLO PARA DESARROLLO"""
    logger.warning("[DEBUG] Se accedió al endpoint de debug de usuarios")
    
    from app.db.models import Usuario
    usuarios = db.query(Usuario).all()

    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u.id,
            "nombre": u.nombre,
            "dni": u.numero_documento,
            "correo": u.correo_universidad,
            "email_verificado": u.email_verificado,
            "universidad": u.universidad,
        })

    logger.info(f"[DEBUG] Total de usuarios: {len(resultado)}")
    return {"total": len(resultado), "usuarios": resultado}
