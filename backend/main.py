from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.db.database import engine, Base

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Login Universitario",
    description="Login con Email/Contraseña y Google OAuth usando el mismo ID",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "mensaje": "API funcionando correctamente",
        "endpoints": {
            "registro": "POST /auth/registro",
            "login": "POST /auth/login",
            "google_login": "POST /auth/google-login",
            "usuarios": "GET /auth/usuarios",
            "docs": "GET /docs"
        }
    }