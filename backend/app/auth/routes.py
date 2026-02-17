from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from backend.app.schemas.usuario import Usuario, Creditos, Materia, Inscripcion
import hashlib

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def hash_password(password):
    """Hashea la contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()

def get_db():
    return SessionLocal()

# ==================== AUTENTICACIÓN ====================

@auth_bp.route('/registro', methods=['POST'])
def registro():
    """
    Registro de nuevo usuario
    
    Body:
    {
        "nombre": "Juan Pérez",
        "email": "juan@example.com",
        "contraseña": "password123"
    }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Se requiere JSON en el body'}), 400
    
    email = data.get('email', '').strip()
    nombre = data.get('nombre', '').strip()
    contraseña = data.get('contraseña', '').strip()
    
    # Validar datos
    if not email or not nombre or not contraseña:
        return jsonify({'error': 'Email, nombre y contraseña son requeridos'}), 400
    
    if len(contraseña) < 6:
        return jsonify({'error': 'La contraseña debe tener al menos 6 caracteres'}), 400
    
    if '@' not in email:
        return jsonify({'error': 'Email inválido'}), 400
    
    db = get_db()
    try:
        # Verificar si el email ya existe
        usuario_existe = db.query(Usuario).filter(Usuario.email == email).first()
        if usuario_existe:
            return jsonify({'error': 'Este email ya está registrado'}), 400
        
        # Crear nuevo usuario
        nuevo_usuario = Usuario(
            email=email,
            nombre=nombre,
            contraseña_hash=hash_password(contraseña),
            email_verificado=True
        )
        db.add(nuevo_usuario)
        db.flush()
        
        # Crear registro de créditos
        creditos = Creditos(
            usuario_id=nuevo_usuario.id,
            creditos_totales=120,
            creditos_cursados=0,
            creditos_disponibles=120
        )
        db.add(creditos)
        db.commit()
        
        return jsonify({
            'success': True,
            'mensaje': f'Usuario {nombre} registrado exitosamente',
            'usuario': {
                'id': nuevo_usuario.id,
                'email': nuevo_usuario.email,
                'nombre': nuevo_usuario.nombre
            }
        }), 201
    
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return jsonify({'error': 'Error al registrar'}), 500
    finally:
        db.close()

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login con email y contraseña
    
    Body:
    {
        "email": "juan@example.com",
        "contraseña": "password123"
    }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Se requiere JSON en el body'}), 400
    
    email = data.get('email', '').strip()
    contraseña = data.get('contraseña', '').strip()
    
    if not email or not contraseña:
        return jsonify({'error': 'Email y contraseña son requeridos'}), 400
    
    db = get_db()
    try:
        # Buscar usuario
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        
        if not usuario or usuario.contraseña_hash != hash_password(contraseña):
            return jsonify({'error': 'Email o contraseña incorrectos'}), 401
        
        # Guardar en sesión
        session['user_id'] = usuario.id
        session['email'] = usuario.email
        session['nombre'] = usuario.nombre
        
        return jsonify({
            'success': True,
            'mensaje': f'¡Bienvenido {usuario.nombre}!',
            'usuario': {
                'id': usuario.id,
                'email': usuario.email,
                'nombre': usuario.nombre
            }
        }), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Error al iniciar sesión'}), 500
    finally:
        db.close()

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Cierra la sesión"""
    session.clear()
    
    return jsonify({
        'success': True,
        'mensaje': 'Sesión cerrada correctamente'
    }), 200

# ==================== USUARIO ====================

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    """Obtiene la información del usuario actual"""
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'No autenticado'}), 401
    
    db = get_db()
    try:
        usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
        
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        # Obtener información de créditos
        creditos = db.query(Creditos).filter(
            Creditos.usuario_id == user_id
        ).first()
        
        return jsonify({
            'id': usuario.id,
            'email': usuario.email,
            'nombre': usuario.nombre,
            'email_verificado': usuario.email_verificado,
            'creditos': {
                'totales': creditos.creditos_totales if creditos else 120,
                'cursados': creditos.creditos_cursados if creditos else 0,
                'disponibles': creditos.creditos_disponibles if creditos else 120
            }
        }), 200
    finally:
        db.close()

# ==================== CRÉDITOS ====================

@auth_bp.route('/creditos', methods=['GET'])
def get_creditos():
    """Obtiene los créditos del usuario autenticado"""
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'No autenticado'}), 401
    
    db = get_db()
    try:
        creditos = db.query(Creditos).filter(
            Creditos.usuario_id == user_id
        ).first()
        
        if not creditos:
            return jsonify({'error': 'Créditos no encontrados'}), 404
        
        return jsonify({
            'totales': creditos.creditos_totales,
            'cursados': creditos.creditos_cursados,
            'disponibles': creditos.creditos_disponibles
        }), 200
    finally:
        db.close()

# ==================== MATERIAS ====================

@auth_bp.route('/materias', methods=['GET'])
def get_materias():
    """Obtiene todas las materias disponibles"""
    db = get_db()
    try:
        materias = db.query(Materia).all()
        
        return jsonify([{
            'id': m.id,
            'nombre': m.nombre,
            'creditos': m.creditos,
            'semestre': m.semestre
        } for m in materias]), 200
    finally:
        db.close()

@auth_bp.route('/materias/<int:materia_id>', methods=['GET'])
def get_materia(materia_id):
    """Obtiene una materia específica"""
    db = get_db()
    try:
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        
        if not materia:
            return jsonify({'error': 'Materia no encontrada'}), 404
        
        return jsonify({
            'id': materia.id,
            'nombre': materia.nombre,
            'creditos': materia.creditos,
            'semestre': materia.semestre
        }), 200
    finally:
        db.close()

# ==================== INSCRIPCIONES ====================

@auth_bp.route('/inscribirse/<int:materia_id>', methods=['POST'])
def inscribirse_materia(materia_id):
    """
    Inscribe al usuario autenticado en una materia
    
    Parámetros:
    - materia_id: ID de la materia
    """
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'No autenticado'}), 401
    
    db = get_db()
    try:
        # Verificar que la materia existe
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        if not materia:
            return jsonify({'error': 'Materia no encontrada'}), 404
        
        # Verificar que el usuario no esté ya inscrito
        inscripcion_existe = db.query(Inscripcion).filter(
            Inscripcion.usuario_id == user_id,
            Inscripcion.materia_id == materia_id
        ).first()
        
        if inscripcion_existe:
            return jsonify({'error': 'Ya estás inscrito en esta materia'}), 400
        
        # Crear inscripción
        nueva_inscripcion = Inscripcion(
            usuario_id=user_id,
            materia_id=materia_id
        )
        db.add(nueva_inscripcion)
        db.commit()
        
        return jsonify({
            'success': True,
            'mensaje': f'Te has inscrito en {materia.nombre}'
        }), 201
    
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return jsonify({'error': 'Error al inscribirse'}), 500
    finally:
        db.close()

@auth_bp.route('/mis-materias', methods=['GET'])
def mis_materias():
    """Obtiene las materias en las que está inscrito el usuario autenticado"""
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'No autenticado'}), 401
    
    db = get_db()
    try:
        inscripciones = db.query(Inscripcion).filter(
            Inscripcion.usuario_id == user_id
        ).all()
        
        materias = []
        for inscripcion in inscripciones:
            materias.append({
                'id': inscripcion.materia.id,
                'nombre': inscripcion.materia.nombre,
                'creditos': inscripcion.materia.creditos,
                'semestre': inscripcion.materia.semestre,
                'estado': inscripcion.estado,
                'fecha_inscripcion': inscripcion.fecha_inscripcion.isoformat()
            })
        
        return jsonify(materias), 200
    finally:
        db.close()

@auth_bp.route('/desinscribirse/<int:materia_id>', methods=['POST'])
def desinscribirse_materia(materia_id):
    """
    Desinscribe al usuario autenticado de una materia
    
    Parámetros:
    - materia_id: ID de la materia
    """
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'No autenticado'}), 401
    
    db = get_db()
    try:
        # Buscar inscripción
        inscripcion = db.query(Inscripcion).filter(
            Inscripcion.usuario_id == user_id,
            Inscripcion.materia_id == materia_id
        ).first()
        
        if not inscripcion:
            return jsonify({'error': 'No estás inscrito en esta materia'}), 404
        
        # Eliminar inscripción
        db.delete(inscripcion)
        db.commit()
        
        return jsonify({
            'success': True,
            'mensaje': 'Te has desinscrito de la materia'
        }), 200
    
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return jsonify({'error': 'Error al desinscribirse'}), 500
    finally:
        db.close()