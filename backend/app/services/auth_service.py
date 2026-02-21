from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Usuario, EstudianteHabilitado, UsuarioInformation
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin
from app.services.jwt_service import (
    hash_password,
    verify_password,
    generar_token_verificacion,
    crear_access_token,
)
import logging

logger = logging.getLogger(__name__)


class AuthService:
    """Servicio de autenticación - Lógica de registro y login"""

    @staticmethod
    def registrar_usuario(datos: UsuarioRegistro, db: Session) -> dict:
        """Registra un nuevo usuario validando contra estudiantes habilitados"""
        
        # Validaciones básicas
        if datos.contraseña != datos.confirmar_contraseña:
            raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")

        if len(datos.contraseña) < 6:
            raise HTTPException(
                status_code=400, detail="La contraseña debe tener al menos 6 caracteres"
            )

        # Limpiar DNI
        dni = datos.dni.strip().upper()
        if dni.startswith("DNI"):
            dni = dni[3:]
        if dni.startswith("CE"):
            dni = dni[2:]

        # Buscar estudiante habilitado
        estudiante = (
            db.query(EstudianteHabilitado)
            .filter(
                EstudianteHabilitado.universidad == datos.universidad,
                EstudianteHabilitado.numero_documento == dni,
                EstudianteHabilitado.correo_universidad == datos.correo_universidad,
            )
            .first()
        )

        if not estudiante:
            raise HTTPException(
                status_code=403,
                detail="No estás habilitado para registrarte. Verifica que tu Universidad, DNI y Email sean correctos.",
            )

        # Verificar fechas de habilitación
        hoy = date.today()
        if not (
            estudiante.fecha_inicio_habilitacion <= hoy <= estudiante.fecha_fin_habilitacion
        ):
            raise HTTPException(
                status_code=403, detail="Tu habilitación ha expirado o aún no ha iniciado."
            )

        # Verificar si ya está registrado
        usuario_existe = (
            db.query(Usuario)
            .filter(Usuario.numero_documento == estudiante.numero_documento)
            .first()
        )

        if usuario_existe:
            raise HTTPException(status_code=400, detail="Ya estás registrado.")

        # Crear usuario
        token = generar_token_verificacion()
        nuevo_usuario = Usuario(
            universidad=estudiante.universidad,
            numero_documento=estudiante.numero_documento,
            tipo_documento=estudiante.tipo_documento,
            nombre=estudiante.nombre,
            segundo_nombre=estudiante.segundo_nombre,
            apellido_paterno=estudiante.apellido_paterno,
            apellido_materno=estudiante.apellido_materno,
            correo_universidad=estudiante.correo_universidad,
            contraseña_hash=hash_password(datos.contraseña),
            email_verificado=True,
            token_verificacion=token,
        )

        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        # Crear token de acceso JWT
        access_token = crear_access_token(data={"sub": str(nuevo_usuario.id)})

        logger.info(f"[AUTH-SERVICE] ✓ Usuario registrado: {nuevo_usuario.nombre}")

        return {
            "success": True,
            "mensaje": f"Registro exitoso. Bienvenido {nuevo_usuario.nombre}",
            "access_token": access_token,
            "token_type": "bearer",
            "usuario": AuthService._formato_usuario(nuevo_usuario),
        }

    @staticmethod
    def login_usuario(datos: UsuarioLogin, db: Session) -> dict:
        """Realiza login y genera JWT token"""
        logger.info(f"[AUTH-SERVICE] Solicitud de login recibida")

        # Limpiar DNI
        dni = datos.dni.strip().upper()
        if dni.startswith("DNI"):
            dni = dni[3:]
        if dni.startswith("CE"):
            dni = dni[2:]

        # Buscar usuario
        logger.info(f"[AUTH-SERVICE] Buscando usuario con DNI: {dni[:3]}***")
        usuario = db.query(Usuario).filter(Usuario.numero_documento == dni).first()

        if not usuario:
            logger.warning(f"[AUTH-SERVICE] Usuario no encontrado con DNI: {dni[:3]}***")
            raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")

        logger.info(f"[AUTH-SERVICE] Usuario encontrado: {usuario.nombre}")

        # Verificar contraseña
        logger.info(f"[AUTH-SERVICE] Verificando contraseña...")
        if not verify_password(datos.contraseña, usuario.contraseña_hash):
            logger.warning(f"[AUTH-SERVICE] Contraseña incorrecta para usuario: {usuario.nombre}")
            raise HTTPException(status_code=401, detail="DNI o contraseña incorrectos")

        logger.info(f"[AUTH-SERVICE] Contraseña verificada correctamente")

        if not usuario.email_verificado:
            logger.warning(f"[AUTH-SERVICE] Email NO verificado para usuario: {usuario.nombre}")
            raise HTTPException(
                status_code=403, detail="Debes verificar tu correo antes de iniciar sesión."
            )

        # Crear JWT token
        logger.info(f"[AUTH-SERVICE] Creando JWT token para usuario: {usuario.nombre}")
        access_token = crear_access_token(data={"sub": str(usuario.id)})

        logger.info(f"[AUTH-SERVICE] ✅ Login exitoso para usuario: {usuario.nombre}")

        return {
            "success": True,
            "mensaje": f"¡Bienvenido {usuario.nombre}!",
            "access_token": access_token,
            "token_type": "bearer",
            "usuario": AuthService._formato_usuario(usuario),
        }

    @staticmethod
    def _formato_usuario(usuario: Usuario) -> dict:
        """Formato estándar de usuario para respuestas"""
        return {
            "id": usuario.id,
            "universidad": usuario.universidad,
            "numero_documento": usuario.numero_documento,
            "tipo_documento": usuario.tipo_documento,
            "nombre": usuario.nombre,
            "segundo_nombre": usuario.segundo_nombre,
            "apellido_paterno": usuario.apellido_paterno,
            "apellido_materno": usuario.apellido_materno,
            "apellidos": f"{usuario.apellido_paterno} {usuario.apellido_materno}",
            "correo_universidad": usuario.correo_universidad,
            "email_verificado": usuario.email_verificado,
        }
