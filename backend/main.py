from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.db.database import engine, Base

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Crédito Universitario")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "mensaje": "API Crédito Universitario - SQLite",
        "bd": "creditos_uni.db",
        "docs": "/docs"
    }