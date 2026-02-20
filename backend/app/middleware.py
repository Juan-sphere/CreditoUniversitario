"""
Configuración centralizada de middleware
"""

from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.config import es_ruta_publica


class MiddlewareAutenticacion(BaseHTTPMiddleware):
    """
    Middleware personalizado para validar rutas públicas/privadas
    Puedes agregar lógica de autenticación aquí si lo necesitas
    """

    async def dispatch(self, request: Request, call_next):
        ruta = request.url.path
        es_publica = es_ruta_publica(ruta)

        # Registrar si es pública o privada
        request.state.es_ruta_publica = es_publica

        response = await call_next(request)
        return response


def setup_middleware(app):
    """Configurar todos los middleware de la aplicación"""

    # Middleware personalizado de autenticación
    app.add_middleware(MiddlewareAutenticacion)

    # CORS Middleware - Permitir solicitudes desde el frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "*"
        ],  # En producción, especificar dominio: ["https://tudominio.com"]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
