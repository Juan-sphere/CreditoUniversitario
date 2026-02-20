import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tu-clave-secreta-super-segura")
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


# ==================== CONFIGURACIÓN DE RUTAS ====================

RUTAS_PUBLICAS = [
    "/",
    "/docs",
    "/openapi.json",
    "/auth/registro",
    "/auth/login",
    "/auth/verificar",
    "/auth/universidades",  # Listar universidades sin autenticación
    "/auth/buscar-estudiante",  # Buscar estudiante por DNI sin autenticación
]

# Prefijos de rutas públicas (rutas que comienzan con estos prefijos son públicas)
PREFIJOS_PUBLICOS = [
    "/docs",
    "/redoc",
    "/openapi.json",
]


def es_ruta_publica(ruta: str) -> bool:
    """
    Verifica si una ruta es pública (no requiere autenticación)

    Args:
        ruta: Ruta a verificar (ej: "/auth/login")

    Returns:
        True si la ruta es pública, False si requiere token
    """
    # Verificar rutas exactas
    if ruta in RUTAS_PUBLICAS:
        return True

    # Verificar prefijos
    for prefijo in PREFIJOS_PUBLICOS:
        if ruta.startswith(prefijo):
            return True

    if ruta.startswith("/auth/") and ruta not in ["/auth/usuarios", "/auth/admin"]:
        return True

    return False
