from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.db.database import engine, Base
from app.middleware import setup_middleware

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema Crédito Universitario",
    description="API para gestión de créditos universitarios",
    version="1.0.0",
)

# Configurar middleware
setup_middleware(app)

# Incluir routers
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "mensaje": "API Crédito Universitario - SQLite",
        "bd": "creditos_uni.db",
        "docs": "/docs",
    }
