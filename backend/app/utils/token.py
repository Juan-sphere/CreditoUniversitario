from typing import Optional
from fastapi import Header, HTTPException
import logging

logger = logging.getLogger(__name__)


def get_token_from_header(authorization: Optional[str] = Header(None)) -> str:
    """Extrae el token del header Authorization: Bearer <token>"""
    logger.info(f"[AUTH] Header Authorization recibido: {authorization[:50] if authorization else 'NINGUNO'}...")

    if not authorization:
        logger.warning("[AUTH] ❌ No se recibió header Authorization")
        raise HTTPException(
            status_code=401, detail="Token requerido en el header Authorization"
        )

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        logger.warning(f"[AUTH] ❌ Formato inválido: {authorization[:30]}...")
        raise HTTPException(
            status_code=401,
            detail="Formato inválido. Use: Authorization: Bearer <token>",
        )

    logger.info(f"[AUTH] ✓ Token extraído correctamente")
    return parts[1]
