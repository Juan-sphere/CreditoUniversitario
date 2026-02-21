from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from app.db.database import get_db
from app.schemas.usuario import (
    UsuarioRegistro,
    UsuarioLogin,
    InformacionPersonalUpdate,
)
from app.schemas.parent import (
    ParentInformationCreate,
    ParentInformationUpdate,
    ParentTypeEnum,
)
from app.schemas.family import (
    FamilyInformationCreate,
    FamilyInformationUpdate,
)
from app.services.auth_service import AuthService
from app.services.informacion_personal_service import InformacionPersonalService
from app.services.estudiante_service import EstudianteService
from app.services.parent_service import ParentService
from app.services.family_service import FamilyService
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


# ==================== INFORMACIÓN DE PADRES ====================
@router.post("/informacion-padres")
def guardar_padre(
    datos: ParentInformationCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Guarda o actualiza la información de un progenitor"""
    logger.info(f"[PADRE] POST /informacion-padres - Guardando información de {datos.parent_type.value}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[PADRE] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[PADRE] ❌ Error de autenticación: {str(e)}")
        raise

    return ParentService.guardar_or_actualizar_padre(usuario, datos, db)


@router.put("/informacion-padres")
def actualizar_padre(
    datos: ParentInformationCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Actualiza la información de un progenitor existente"""
    logger.info(f"[PADRE] PUT /informacion-padres - Actualizando información de {datos.parent_type.value}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[PADRE] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[PADRE] ❌ Error de autenticación: {str(e)}")
        raise

    return ParentService.guardar_or_actualizar_padre(usuario, datos, db)


@router.get("/informacion-padres")
def obtener_padres(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Obtiene la información de los progenitores"""
    logger.info("[PADRE] GET /informacion-padres - Obteniendo información de padres")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[PADRE] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[PADRE] ❌ Error de autenticación: {str(e)}")
        raise

    return ParentService.obtener_padres(usuario, db)


@router.delete("/informacion-padres/{parent_type}")
def eliminar_padre(
    parent_type: ParentTypeEnum,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Elimina la información de un progenitor"""
    logger.info(f"[PADRE] DELETE /informacion-padres/{parent_type.value}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[PADRE] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[PADRE] ❌ Error de autenticación: {str(e)}")
        raise

    return ParentService.eliminar_padre(usuario, parent_type, db)


# ==================== INFORMACIÓN DE FAMILIARES ====================
@router.post("/composicion-familiar")
def crear_familiar(
    datos: FamilyInformationCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Crea un nuevo familiar para el usuario"""
    logger.info("[FAMILY] POST /composicion-familiar - Creando nuevo familiar")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[FAMILY] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[FAMILY] ❌ Error de autenticación: {str(e)}")
        raise

    return FamilyService.crear_familiar(usuario, datos, db)


@router.get("/composicion-familiar")
def obtener_familiares(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Obtiene todos los familiares del usuario"""
    logger.info("[FAMILY] GET /composicion-familiar - Obteniendo familiares")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[FAMILY] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[FAMILY] ❌ Error de autenticación: {str(e)}")
        raise

    return FamilyService.obtener_familiares(usuario, db)


@router.get("/composicion-familiar/{familiar_id}")
def obtener_familiar(
    familiar_id: int,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Obtiene un familiar específico"""
    logger.info(f"[FAMILY] GET /composicion-familiar/{familiar_id}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[FAMILY] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[FAMILY] ❌ Error de autenticación: {str(e)}")
        raise

    return FamilyService.obtener_familiar(usuario, familiar_id, db)


@router.put("/composicion-familiar/{familiar_id}")
def actualizar_familiar(
    familiar_id: int,
    datos: FamilyInformationUpdate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Actualiza la información de un familiar"""
    logger.info(f"[FAMILY] PUT /composicion-familiar/{familiar_id}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[FAMILY] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[FAMILY] ❌ Error de autenticación: {str(e)}")
        raise

    return FamilyService.actualizar_familiar(usuario, familiar_id, datos, db)


@router.delete("/composicion-familiar/{familiar_id}")
def eliminar_familiar(
    familiar_id: int,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Elimina un familiar"""
    logger.info(f"[FAMILY] DELETE /composicion-familiar/{familiar_id}")

    try:
        token = get_token_from_header(authorization)
        usuario = get_current_user(token, db)
        logger.info(f"[FAMILY] Usuario autenticado: {usuario.nombre}")
    except Exception as e:
        logger.error(f"[FAMILY] ❌ Error de autenticación: {str(e)}")
        raise

    return FamilyService.eliminar_familiar(usuario, familiar_id, db)


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
