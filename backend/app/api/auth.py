from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Usuario
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin, GoogleLoginRequest
from google.oauth2 import id_token
from google.auth.transport import requests
import hashlib
import os

router = APIRouter(prefix="/auth", tags=["auth"])

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

def hash_password(password: str) -> str:
    """Hashea la contraseña con SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

# ==================== REGISTRO CON EMAIL/CONTRASEÑA ====================
@router.post("/registro")
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    """
    Registro con email y contraseña
    
    Body:
    {
        "email": "juan@example.com",
        "nombre": "Juan Pérez",
        "contraseña": "password123"
    }
    """
    # Validaciones
    if len(datos.contraseña) < 6:
        raise HTTPException(
            status_code=400, 
            detail="La contraseña debe tener al menos 6 caracteres"
        )
    
    # Verificar si el email ya existe
    usuario_existe = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="Este email ya está registrado")
    
    # Crear usuario con contraseña
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

# ==================== LOGIN CON EMAIL/CONTRASEÑA ====================
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """
    Login con email y contraseña
    
    Body:
    {
        "email": "juan@example.com",
        "contraseña": "password123"
    }
    """
    # Buscar usuario
    usuario = db.query(Usuario).filter(Usuario.email == datos.email).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")
    
    # Si el usuario solo se registró con Google (no tiene contraseña)
    if not usuario.contraseña_hash:
        raise HTTPException(
            status_code=400,
            detail="Esta cuenta se creó con Google. Usa el botón de Google para iniciar sesión."
        )
    
    # Verificar contraseña
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

# ==================== LOGIN CON GOOGLE (OPCIÓN A) ====================
@router.post("/google-login")
def google_login(datos: GoogleLoginRequest, db: Session = Depends(get_db)):
    """
    Login con Google OAuth (OPCIÓN A - Flexible)
    
    Permite login con Google incluso si el usuario tiene contraseña.
    Mismo email = misma cuenta.
    
    Body:
    {
        "credential": "token-jwt-de-google"
    }
    """
    try:
        # Verificar el token de Google
        idinfo = id_token.verify_oauth2_token(
            datos.credential,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )
        
        email = idinfo['email']
        nombre = idinfo.get('name', email.split('@')[0])
        email_verificado = idinfo.get('email_verified', True)
        
        # Buscar si el usuario ya existe por email
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        
        if usuario:
            # ✅ OPCIÓN A: Lo deja entrar sin importar si tiene contraseña
            # Esto permite que un usuario use AMBOS métodos de login
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
                contraseña_hash=None,  # NULL = solo usa Google
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

# ==================== LISTAR USUARIOS (PARA PRUEBAS) ====================
@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    """
    Lista todos los usuarios indicando su método de autenticación
    """
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "email": u.email,
            "nombre": u.nombre,
            "tiene_contraseña": bool(u.contraseña_hash),
            "metodo": "Google" if not u.contraseña_hash else "Email/Contraseña",
            "puede_usar_ambos": bool(u.contraseña_hash)  # Si tiene contraseña, puede usar ambos
        }
        for u in usuarios
    ]