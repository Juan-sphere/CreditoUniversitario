from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Usuario, EstudianteHabilitado
from app.schemas.usuario import (
    UsuarioRegistro,
    UsuarioLogin,
    EstudianteHabilitadoCreate,
    TokenResponse,
)
from datetime import date, datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

# Configuración JWT
SECRET_KEY = os.getenv("SECRET_KEY", "tu-clave-secreta-aqui-cambiarla-en-produccion")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/auth", tags=["auth"])


# ==================== FUNCIONES DE SEGURIDAD ====================
def hash_password(password: str) -> str:
    """Hash seguro de contraseña con bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica contraseña con soporte para SHA256 heredado y bcrypt nuevo"""
    # Intenta primero con bcrypt
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        pass

    # Si falla, intenta con SHA256 (método antiguo)
    import hashlib

    sha256_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    return sha256_hash == hashed_password


def generar_token_verificacion() -> str:
    """Genera token para verificación de email"""
    import secrets

    return secrets.token_urlsafe(32)


def crear_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Crea JWT token de acceso"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verificar_token(token: str) -> dict:
    """Verifica y decodifica JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: int = payload.get("sub")
        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"usuario_id": usuario_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado o inválido")


def get_current_user(token: str, db: Session = Depends(get_db)):
    """Dependency para obtener usuario actual desde el token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: int = payload.get("sub")
        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado o inválido")

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return usuario


def get_token_from_header(authorization: Optional[str] = Header(None)) -> str:
    """Extrae el token del header Authorization: Bearer <token>"""
    if not authorization:
        raise HTTPException(
            status_code=401, detail="Token requerido en el header Authorization"
        )

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=401,
            detail="Formato inválido. Use: Authorization: Bearer <token>",
        )

    return parts[1]


# ==================== REGISTRO ====================
@router.post("/registro")
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    """
    Registro de estudiante habilitado
    Valida: Universidad + DNI + Email deben estar en la BD de habilitados
    """

    # Validaciones básicas
    if datos.contraseña != datos.confirmar_contraseña:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")

    if len(datos.contraseña) < 6:
        raise HTTPException(
            status_code=400, detail="La contraseña debe tener al menos 6 caracteres"
        )

    # Limpiar DNI (remover "DNI" si viene)
    dni = datos.dni.strip().upper()
    if dni.startswith("DNI"):
        dni = dni[3:]
    if dni.startswith("CE"):
        dni = dni[2:]

    # Buscar estudiante habilitado
    estudiante = (
        db.query(EstudianteHabilitado)
        .filter(
            EstudianteHabilitado.universidad == datos.universidad,
            EstudianteHabilitado.numero_documento == dni,
            EstudianteHabilitado.correo_universidad == datos.correo_universidad,
        )
        .first()
    )

    if not estudiante:
        raise HTTPException(
            status_code=403,
            detail="No estás habilitado para registrarte. Verifica que tu Universidad, DNI y Email sean correctos.",
        )

    # Verificar fechas de habilitación
    hoy = date.today()
    if not (
        estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion
    ):
        raise HTTPException(
            status_code=403, detail="Tu habilitación ha expirado o aún no ha iniciado."
        )

    # Verificar si ya está registrado
    usuario_existe = (
        db.query(Usuario)
        .filter(Usuario.numero_documento == estudiante.numero_documento)
        .first()
    )

    if usuario_existe:
        raise HTTPException(status_code=400, detail="Ya estás registrado.")

    # Crear usuario
    token = generar_token_verificacion()
    nuevo_usuario = Usuario(
        universidad=estudiante.universidad,
        numero_documento=estudiante.numero_documento,
        tipo_documento=estudiante.tipo_documento,
        nombre=estudiante.nombre,
        segundo_nombre=estudiante.segundo_nombre,
        apellido_paterno=estudiante.apellido_paterno,
        apellido_materno=estudiante.apellido_materno,
        correo_universidad=estudiante.correo_universidad,
        contraseña_hash=hash_password(datos.contraseña),
        email_verificado=True,  # Cambiar a False cuando implementes emails
        token_verificacion=token,
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    # Crear token de acceso JWT
    access_token = crear_access_token(data={"sub": nuevo_usuario.id})

    return {
        "success": True,
        "mensaje": f"Registro exitoso. Bienvenido {nuevo_usuario.nombre}",
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": {
            "id": nuevo_usuario.id,
            "universidad": nuevo_usuario.universidad,
            "numero_documento": nuevo_usuario.numero_documento,
            "tipo_documento": nuevo_usuario.tipo_documento,
            "nombre": nuevo_usuario.nombre,
            "segundo_nombre": nuevo_usuario.segundo_nombre,
            "apellido_paterno": nuevo_usuario.apellido_paterno,
            "apellido_materno": nuevo_usuario.apellido_materno,
            "apellidos": f"{nuevo_usuario.apellido_paterno} {nuevo_usuario.apellido_materno}",
            "correo_universidad": nuevo_usuario.correo_universidad,
            "email_verificado": nuevo_usuario.email_verificado,
        },
    }


# ==================== LOGIN ====================
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """Login con DNI y generación de JWT token"""

    # Limpiar DNI
    dni = datos.dni.strip().upper()
    if dni.startswith("DNI"):
        dni = dni[3:]
    if dni.startswith("CE"):
        dni = dni[2:]

    # Buscar usuario
    usuario = db.query(Usuario).filter(Usuario.numero_documento == dni).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")

    # Verificar contraseña con bcrypt
    if not verify_password(datos.contraseña, usuario.contraseña_hash):
        raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")

    if not usuario.email_verificado:
        raise HTTPException(
            status_code=403, detail="Debes verificar tu correo antes de iniciar sesión."
        )

    # Crear JWT token
    access_token = crear_access_token(data={"sub": usuario.id})

    return {
        "success": True,
        "mensaje": f"¡Bienvenido {usuario.nombre}!",
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": {
            "id": usuario.id,
            "universidad": usuario.universidad,
            "numero_documento": usuario.numero_documento,
            "tipo_documento": usuario.tipo_documento,
            "nombre": usuario.nombre,
            "segundo_nombre": usuario.segundo_nombre,
            "apellido_paterno": usuario.apellido_paterno,
            "apellido_materno": usuario.apellido_materno,
            "apellidos": f"{usuario.apellido_paterno} {usuario.apellido_materno}",
            "correo_universidad": usuario.correo_universidad,
            "email_verificado": usuario.email_verificado,
        },
    }


# ==================== OBTENER USUARIO ACTUAL ====================
@router.get("/me")
def obtener_usuario_actual(
    authorization: Optional[str] = Header(None), db: Session = Depends(get_db)
):
    """Obtener información del usuario autenticado"""
    token = get_token_from_header(authorization)
    usuario = get_current_user(token, db)

    return {
        "success": True,
        "usuario": {
            "id": usuario.id,
            "universidad": usuario.universidad,
            "numero_documento": usuario.numero_documento,
            "nombre": usuario.nombre,
            "segundo_nombre": usuario.segundo_nombre,
            "apellidos": f"{usuario.apellido_paterno} {usuario.apellido_materno}",
            "correo_universidad": usuario.correo_universidad,
            "email_verificado": usuario.email_verificado,
        },
    }


# ==================== REFRESCAR TOKEN ====================
@router.post("/refresh")
def refrescar_token(
    authorization: Optional[str] = Header(None), db: Session = Depends(get_db)
):
    """Refrescar JWT token"""
    token = get_token_from_header(authorization)
    usuario = get_current_user(token, db)

    # Crear nuevo token
    new_access_token = crear_access_token(data={"sub": usuario.id})

    return {"success": True, "access_token": new_access_token, "token_type": "bearer"}


# ==================== VERIFICAR EMAIL ====================
@router.get("/verificar/{token}")
def verificar_email(token: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.token_verificacion == token).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Token inválido")

    usuario.email_verificado = True
    usuario.token_verificacion = None
    db.commit()

    return {"success": True, "mensaje": "Cuenta verificada. Ya puedes iniciar sesión."}


# ==================== LISTAR USUARIOS ====================
@router.get("/usuarios")
def listar_usuarios(
    authorization: Optional[str] = Header(None), db: Session = Depends(get_db)
):
    """Listar todos los usuarios (requiere autenticación)"""
    token = get_token_from_header(authorization)
    get_current_user(token, db)  # Verificar que el token es válido

    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "universidad": u.universidad,
            "documento": f"{u.tipo_documento}{u.numero_documento}",
            "nombre": f"{u.nombre} {u.apellido_paterno} {u.apellido_materno}",
            "email_verificado": u.email_verificado,
        }
        for u in usuarios
    ]


# ==================== ADMIN: AGREGAR ESTUDIANTE ====================
@router.post("/admin/estudiante")
def crear_estudiante(
    datos: EstudianteHabilitadoCreate,
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """Crear estudiante habilitado (requiere autenticación)"""
    token = get_token_from_header(authorization)
    get_current_user(token, db)  # Verificar que el token es válido

    estudiante = EstudianteHabilitado(**datos.dict())
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return {"success": True, "estudiante_id": estudiante.id}


# ==================== ADMIN: CARGAR EXCEL ====================
@router.post("/admin/cargar-excel")
async def cargar_excel_estudiantes(
    authorization: Optional[str] = Header(None), file: bytes = None
):
    """
    Cargar Excel con estudiantes habilitados (requiere autenticación)
    Columnas esperadas: Universidad, DNI, Apellido Paterno, Apellido Materno,
                        Nombre, Segundo Nombre, Email Universidad
    """
    token = get_token_from_header(authorization)
    # TODO: Validar usuario con get_current_user cuando tengamos DB
    # Implementar con pandas cuando sea necesario
    return {"success": True, "mensaje": "Endpoint pendiente de implementar"}


# ==================== OBTENER UNIVERSIDADES ====================
@router.get("/universidades")
def listar_universidades(db: Session = Depends(get_db)):
    """Obtener lista de universidades disponibles (sin requerir autenticación)"""
    universidades = db.query(EstudianteHabilitado.universidad).distinct().all()
    return [u[0] for u in universidades]


# ==================== BUSCAR ESTUDIANTE POR DNI ====================
@router.get("/buscar-estudiante/{dni}")
def buscar_estudiante(dni: str, db: Session = Depends(get_db)):
    """Buscar estudiante habilitado por DNI para autocompletar registro (sin autenticación)"""

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
        raise HTTPException(status_code=404, detail="DNI no encontrado")

    # Verificar fechas
    hoy = date.today()
    if not (
        estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion
    ):
        raise HTTPException(status_code=403, detail="Tu habilitación ha expirado")

    print(
        f"Estudiante encontrado: {estudiante.nombre} {estudiante.apellido_paterno} {estudiante.apellido_materno} {estudiante.correo_universidad}"
    )

    return {
        "universidad": estudiante.universidad,
        "correo_universidad": estudiante.correo_universidad,
        "nombre": estudiante.nombre,
        "segundo_nombre": estudiante.segundo_nombre,
        "apellido_paterno": estudiante.apellido_paterno,
        "apellido_materno": estudiante.apellido_materno,
    }
