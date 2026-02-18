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

# ==================== REGISTRO ====================
@router.post("/registro")
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    if datos.contraseña != datos.confirmar_contraseña:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    if len(datos.contraseña) < 6:
        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 6 caracteres")
    
    identificador = datos.identificador.strip().upper()
    
    # Buscar en estudiantes habilitados
    estudiante = None
    
    if identificador.startswith("DNI") or identificador.startswith("CE"):
        tipo_doc = identificador[:3] if identificador.startswith("DNI") else identificador[:2]
        numero_doc = identificador[3:] if tipo_doc == "DNI" else identificador[2:]
        
        estudiante = db.query(EstudianteHabilitado).filter(
            EstudianteHabilitado.tipo_documento == tipo_doc,
            EstudianteHabilitado.numero_documento == numero_doc
        ).first()
    else:
        estudiante = db.query(EstudianteHabilitado).filter(
            EstudianteHabilitado.codigo_universidad == identificador
        ).first()
    
    if not estudiante:
        raise HTTPException(
            status_code=403,
            detail="No estás habilitado para registrarte. Contacta con la universidad."
        )
    
    # Verificar fechas
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
    token = secrets.token_urlsafe(32)
    nuevo_usuario = Usuario(
        codigo_universidad=estudiante.codigo_universidad,
        numero_documento=estudiante.numero_documento,
        tipo_documento=estudiante.tipo_documento,
        nombres=estudiante.nombres,
        apellido_paterno=estudiante.apellido_paterno,
        apellido_materno=estudiante.apellido_materno,
        correo_universidad=estudiante.correo_universidad,
        contraseña_hash=hash_password(datos.contraseña),
        email_verificado=True,
        token_verificacion=token
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return {
        "success": True,
        "mensaje": f"Registro exitoso. Revisa tu correo {nuevo_usuario.correo_universidad} para verificar tu cuenta.",
        "usuario": {
            "id": nuevo_usuario.id,
            "nombres": nuevo_usuario.nombres,
            "apellidos": f"{nuevo_usuario.apellido_paterno} {nuevo_usuario.apellido_materno}"
        }
    }

# ==================== LOGIN ====================
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    identificador = datos.identificador.strip().upper()
    
    usuario = None
    
    if identificador.startswith("DNI") or identificador.startswith("CE"):
        tipo_doc = identificador[:3] if identificador.startswith("DNI") else identificador[:2]
        numero_doc = identificador[3:] if tipo_doc == "DNI" else identificador[2:]
        
        usuario = db.query(Usuario).filter(
            Usuario.tipo_documento == tipo_doc,
            Usuario.numero_documento == numero_doc
        ).first()
    else:
        usuario = db.query(Usuario).filter(
            Usuario.codigo_universidad == identificador
        ).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    if usuario.contraseña_hash != hash_password(datos.contraseña):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
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
            "nombres": usuario.nombres,
            "apellidos": f"{usuario.apellido_paterno} {usuario.apellido_materno}",
            "codigo": usuario.codigo_universidad
        }
    }

# ==================== VERIFICAR ====================
@router.get("/verificar/{token}")
def verificar_email(token: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.token_verificacion == token).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Token inválido")
    
    usuario.email_verificado = True
    usuario.token_verificacion = None
    db.commit()
    
    return {
        "success": True,
        "mensaje": "Cuenta verificada. Ya puedes iniciar sesión."
    }

# ==================== ADMIN: AGREGAR ESTUDIANTE ====================
@router.post("/admin/estudiante")
def crear_estudiante(datos: EstudianteHabilitadoCreate, db: Session = Depends(get_db)):
    estudiante = EstudianteHabilitado(**datos.dict())
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return {"success": True, "estudiante": estudiante.id}

# ==================== LISTAR ====================
@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "codigo": u.codigo_universidad,
            "documento": f"{u.tipo_documento}{u.numero_documento}",
            "nombres": u.nombres,
            "email_verificado": u.email_verificado
        }
        for u in usuarios
    ]

@router.get("/admin/tokens")
def ver_tokens(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "nombre": u.nombres,
            "token": u.token_verificacion,
            "verificado": u.email_verificado
        }
        for u in usuarios
    ]