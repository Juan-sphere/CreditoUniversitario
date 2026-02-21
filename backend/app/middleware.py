"""
Configuración centralizada de middleware
"""

from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.config import es_ruta_publica
import logging

logger = logging.getLogger(__name__)


class MiddlewareAutenticacion(BaseHTTPMiddleware):
    """
    Middleware personalizado para validar rutas públicas/privadas
    Puedes agregar lógica de autenticación aquí si lo necesitas
    """

    async def dispatch(self, request: Request, call_next):
        ruta = request.url.path
        metodo = request.method
        
        # LOG INMEDIATO
        logger.warning(f"[MIDDLEWARE] ⬇️ SOLICITUD ENTRANTE: {metodo} {ruta}")
        
        try:
            response = await call_next(request)
            logger.warning(f"[MIDDLEWARE] ⬆️ RESPUESTA: {metodo} {ruta} - Status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"[MIDDLEWARE] ❌ Error en {metodo} {ruta}: {str(e)}", exc_info=True)
            raise


def setup_middleware(app):
    """Configurar todos los middleware de la aplicación"""

    logger.info("Configurando middleware...")

    # Middleware personalizado de autenticación
    app.add_middleware(MiddlewareAutenticacion)

    # CORS Middleware - Permitir solicitudes desde el frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    logger.info("Middleware configurado correctamente")
