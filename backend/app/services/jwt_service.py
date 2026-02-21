import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario
import logging

logger = logging.getLogger(__name__)

# Configuración JWT
SECRET_KEY = os.getenv("SECRET_KEY", "4484455445")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# Contexto para hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash seguro de contraseña con bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica contraseña con soporte para SHA256 heredado y bcrypt nuevo"""
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        pass

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
    logger.info(f"[JWT] Creando token con SECRET_KEY: {SECRET_KEY[:10]}...")
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verificar_token(token: str) -> dict:
    """Verifica y decodifica JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id_str = payload.get("sub")
        if usuario_id_str is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"usuario_id": int(usuario_id_str)}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado o inválido")
    except ValueError:
        raise HTTPException(status_code=401, detail="Token inválido")


def get_current_user(token: str, db: Session):
    """Dependency para obtener usuario actual desde el token"""
    logger.info(f"[JWT] Verificando token con SECRET_KEY: {SECRET_KEY[:10]}...")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id_str = payload.get("sub")
        logger.info(f"[JWT] Token decodificado, usuario_id: {usuario_id_str}")
        if usuario_id_str is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        usuario_id = int(usuario_id_str)
    except JWTError as e:
        logger.error(f"[JWT] ❌ JWTError: {str(e)}")
        raise HTTPException(status_code=401, detail="Token expirado o inválido")
    except ValueError:
        logger.error(f"[JWT] ❌ usuario_id no es un número válido")
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return usuario
