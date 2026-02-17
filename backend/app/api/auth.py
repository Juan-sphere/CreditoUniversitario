from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin, GoogleLoginRequest
from app.db.models import Usuario
from google.oauth2 import id_token
from google.auth.transport import requests
import hashlib
import os

router = APIRouter(prefix="/auth", tags=["auth"])

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# ────────────────────────────────────────────────────────
# REGISTRO CON EMAIL/CONTRASEÑA
# ────────────────────────────────────────────────────────
@router.post("/registro")
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    # Verificar si el email ya existe
    usuario_existe = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="Este email ya está registrado")
    
    if len(datos.contraseña) < 6:
        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 6 caracteres")
    
    # Crear nuevo usuario
    nuevo_usuario = Usuario(
        email=datos.email,
        nombre=datos.nombre,
        contraseña_hash=hash_password(datos.contraseña),
        email_verificado=True
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return {
        "success": True,
        "mensaje": f"Usuario {datos.nombre} registrado exitosamente",
        "usuario": {
            "id": nuevo_usuario.id,
            "email": nuevo_usuario.email,
            "nombre": nuevo_usuario.nombre
        }
    }

# ────────────────────────────────────────────────────────
# LOGIN CON EMAIL/CONTRASEÑA
# ────────────────────────────────────────────────────────
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    # Buscar usuario
    usuario = db.query(Usuario).filter(Usuario.email == datos.email).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")
    
    # Si el usuario se registró con Google, no tiene contraseña
    if not usuario.contraseña_hash:
        raise HTTPException(
            status_code=400, 
            detail="Esta cuenta usa Google. Inicia sesión con Google."
        )
    
    if usuario.contraseña_hash != hash_password(datos.contraseña):
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")
    
    return {
        "success": True,
        "mensaje": f"¡Bienvenido {usuario.nombre}!",
        "usuario": {
            "id": usuario.id,
            "email": usuario.email,
            "nombre": usuario.nombre
        }
    }

# ────────────────────────────────────────────────────────
# LOGIN CON GOOGLE OAUTH
# ────────────────────────────────────────────────────────
@router.post("/google-login")
def google_login(datos: GoogleLoginRequest, db: Session = Depends(get_db)):
    try:
        # Verificar el token de Google
        idinfo = id_token.verify_oauth2_token(
            datos.credential,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )
        
        email = idinfo['email']
        nombre = idinfo.get('name', email.split('@')[0])
        email_verificado = idinfo.get('email_verified', False)
        
        # Buscar usuario por email
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        
        if usuario:
            # Usuario ya existe
            return {
                "success": True,
                "mensaje": f"¡Bienvenido de nuevo {usuario.nombre}!",
                "usuario": {
                    "id": usuario.id,
                    "email": usuario.email,
                    "nombre": usuario.nombre
                }
            }
        else:
            # Crear nuevo usuario con Google (sin contraseña)
            nuevo_usuario = Usuario(
                email=email,
                nombre=nombre,
                contraseña_hash=None,  # Sin contraseña porque usa Google
                email_verificado=email_verificado
            )
            db.add(nuevo_usuario)
            db.commit()
            db.refresh(nuevo_usuario)
            
            return {
                "success": True,
                "mensaje": f"¡Bienvenido {nuevo_usuario.nombre}!",
                "nuevo": True,
                "usuario": {
                    "id": nuevo_usuario.id,
                    "email": nuevo_usuario.email,
                    "nombre": nuevo_usuario.nombre
                }
            }
    
    except ValueError as e:
        raise HTTPException(status_code=401, detail=f"Token de Google inválido: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar login: {str(e)}")

# ────────────────────────────────────────────────────────
# LISTAR USUARIOS (para pruebas)
# ────────────────────────────────────────────────────────
@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "email": u.email,
            "nombre": u.nombre,
            "tiene_contraseña": bool(u.contraseña_hash),
            "usa_google": not bool(u.contraseña_hash)
        }
        for u in usuarios
    ]