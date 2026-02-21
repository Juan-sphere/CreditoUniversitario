from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.db.database import engine, Base
from app.middleware import setup_middleware
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Crear tablas
logger.info("Iniciando aplicación...")
Base.metadata.create_all(bind=engine)
logger.info("Tablas creadas/verificadas")

app = FastAPI(
    title="Sistema Crédito Universitario",
    description="API para gestión de créditos universitarios",
    version="1.0.0",
)

# Configurar middleware
setup_middleware(app)

# Incluir routers
app.include_router(auth_router)
logger.info("Routers incluidos")


@app.get("/")
def root():
    logger.warning("[ROOT] GET / - Root endpoint")
    return {
        "mensaje": "API Crédito Universitario - SQLite",
        "bd": "creditos_uni.db",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    logger.warning("🏥 [HEALTH] GET /health - Health check!")
    return {
        "status": "ok",
        "message": "Server is alive and running!",
        "timestamp": __import__("datetime").datetime.now().isoformat()
    }
