from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Usuario, EstudianteHabilitado
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin, EstudianteHabilitadoCreate
from datetime import date
import hashlib
import secrets

router = APIRouter(prefix="/auth", tags=["auth"])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def generar_token() -> str:
    return secrets.token_urlsafe(32)

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
        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 6 caracteres")
    
    # Limpiar DNI (remover "DNI" si viene)
    dni = datos.dni.strip().upper()
    if dni.startswith("DNI"):
        dni = dni[3:]
    if dni.startswith("CE"):
        dni = dni[2:]
    
    # Buscar estudiante habilitado
    estudiante = db.query(EstudianteHabilitado).filter(
        EstudianteHabilitado.universidad == datos.universidad,
        EstudianteHabilitado.numero_documento == dni,
        EstudianteHabilitado.correo_universidad == datos.correo_universidad
    ).first()
    
    if not estudiante:
        raise HTTPException(
            status_code=403,
            detail="No estás habilitado para registrarte. Verifica que tu Universidad, DNI y Email sean correctos."
        )
    
    # Verificar fechas de habilitación
    hoy = date.today()
    if not (estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion):
        raise HTTPException(
            status_code=403,
            detail="Tu habilitación ha expirado o aún no ha iniciado."
        )
    
    # Verificar si ya está registrado
    usuario_existe = db.query(Usuario).filter(
        Usuario.numero_documento == estudiante.numero_documento
    ).first()
    
    if usuario_existe:
        raise HTTPException(status_code=400, detail="Ya estás registrado.")
    
    # Crear usuario
    token = generar_token()
    nuevo_usuario = Usuario(
        universidad=estudiante.universidad,
        numero_documento=estudiante.numero_documento,
        tipo_documento=estudiante.tipo_documento,
        nombres=estudiante.nombres,
        apellido_paterno=estudiante.apellido_paterno,
        apellido_materno=estudiante.apellido_materno,
        correo_universidad=estudiante.correo_universidad,
        contraseña_hash=hash_password(datos.contraseña),
        email_verificado=True,  # Cambiar a False cuando implementes emails
        token_verificacion=token
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return {
        "success": True,
        "mensaje": f"Registro exitoso. Bienvenido {nuevo_usuario.nombres}",
        "usuario": {
            "id": nuevo_usuario.id,
            "universidad": nuevo_usuario.universidad,
            "nombres": nuevo_usuario.nombres,
            "apellidos": f"{nuevo_usuario.apellido_paterno} {nuevo_usuario.apellido_materno}"
        }
    }

# ==================== LOGIN ====================
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """Login con DNI"""
    
    # Limpiar DNI
    dni = datos.dni.strip().upper()
    if dni.startswith("DNI"):
        dni = dni[3:]
    if dni.startswith("CE"):
        dni = dni[2:]
    
    # Buscar usuario
    usuario = db.query(Usuario).filter(
        Usuario.numero_documento == dni
    ).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")
    
    # Verificar contraseña
    if usuario.contraseña_hash != hash_password(datos.contraseña):
        raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")
    
    if not usuario.email_verificado:
        raise HTTPException(
            status_code=403,
            detail="Debes verificar tu correo antes de iniciar sesión."
        )
    
    return {
        "success": True,
        "mensaje": f"¡Bienvenido {usuario.nombres}!",
        "usuario": {
            "id": usuario.id,
            "universidad": usuario.universidad,
            "nombres": usuario.nombres,
            "apellidos": f"{usuario.apellido_paterno} {usuario.apellido_materno}",
            "correo": usuario.correo_universidad
        }
    }

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
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "universidad": u.universidad,
            "documento": f"{u.tipo_documento}{u.numero_documento}",
            "nombres": f"{u.nombres} {u.apellido_paterno} {u.apellido_materno}",
            "email_verificado": u.email_verificado
        }
        for u in usuarios
    ]

# ==================== ADMIN: AGREGAR ESTUDIANTE ====================
@router.post("/admin/estudiante")
def crear_estudiante(datos: EstudianteHabilitadoCreate, db: Session = Depends(get_db)):
    estudiante = EstudianteHabilitado(**datos.dict())
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return {"success": True, "estudiante_id": estudiante.id}

# ==================== ADMIN: CARGAR EXCEL ====================
@router.post("/admin/cargar-excel")
async def cargar_excel_estudiantes(file: bytes = None):
    """
    TODO: Endpoint para cargar Excel con estudiantes habilitados
    Columnas esperadas: Universidad, DNI, Apellido Paterno, Apellido Materno, 
                        Nombre, Segundo Nombre, Email Universidad
    """
    # Implementar con pandas cuando sea necesario
    return {"success": True, "mensaje": "Endpoint pendiente de implementar"}

# ==================== OBTENER UNIVERSIDADES ====================
@router.get("/universidades")
def listar_universidades(db: Session = Depends(get_db)):
    """Obtener lista de universidades disponibles"""
    universidades = db.query(EstudianteHabilitado.universidad).distinct().all()
    return [u[0] for u in universidades]

    # ==================== BUSCAR ESTUDIANTE POR DNI ====================
@router.get("/buscar-estudiante/{dni}")
def buscar_estudiante(dni: str, db: Session = Depends(get_db)):
    """Buscar estudiante habilitado por DNI para autocompletar registro"""
    
    # Limpiar DNI
    dni_limpio = dni.strip().upper()
    if dni_limpio.startswith("DNI"):
        dni_limpio = dni_limpio[3:]
    if dni_limpio.startswith("CE"):
        dni_limpio = dni_limpio[2:]
    
    # Buscar estudiante
    estudiante = db.query(EstudianteHabilitado).filter(
        EstudianteHabilitado.numero_documento == dni_limpio
    ).first()
    
    if not estudiante:
        raise HTTPException(status_code=404, detail="DNI no encontrado")
    
    # Verificar fechas
    hoy = date.today()
    if not (estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion):
        raise HTTPException(
            status_code=403,
            detail="Tu habilitación ha expirado"
        )
    
    return {
        "universidad": estudiante.universidad,
        "correo_universidad": estudiante.correo_universidad,
        "nombres": estudiante.nombres,
        "apellido_paterno": estudiante.apellido_paterno,
        "apellido_materno": estudiante.apellido_materno
    }