from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Usuario, Creditos, Materia, Inscripcion
import hashlib

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def hash_password(password):
    """Hashea la contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()

def get_db():
    return SessionLocal()

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login con email y contraseña"""
    data = request.get_json()
    email = data.get('email')
    contraseña = data.get('contraseña')
    
    if not email or not contraseña:
        return jsonify({'error': 'Email y contraseña requeridos'}), 400
    
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
            'mensaje': f"¡Bienvenido {usuario.nombre}!",
            'usuario': {
                'id': usuario.id,
                'email': usuario.email,
                'nombre': usuario.nombre
            }
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Error al iniciar sesión'}), 500
    finally:
        db.close()

@auth_bp.route('/registro', methods=['POST'])
def registro():
    """Registro de nuevo usuario"""
    data = request.get_json()
    email = data.get('email')
    nombre = data.get('nombre')
    contraseña = data.get('contraseña')
    
    if not email or not nombre or not contraseña:
        return jsonify({'error': 'Todos los campos son requeridos'}), 400
    
    if len(contraseña) < 6:
        return jsonify({'error': 'La contraseña debe tener al menos 6 caracteres'}), 400
    
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
            'mensaje': f'Usuario {nombre} registrado exitosamente'
        })
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return jsonify({'error': 'Error al registrar'}), 500
    finally:
        db.close()

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Cierra la sesión"""
    session.clear()
    
    return jsonify({
        'success': True,
        'mensaje': 'Sesión cerrada correctamente'
    })

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
            'creditos': {
                'totales': creditos.creditos_totales if creditos else 120,
                'cursados': creditos.creditos_cursados if creditos else 0,
                'disponibles': creditos.creditos_disponibles if creditos else 120
            }
        })
    finally:
        db.close()

@auth_bp.route('/creditos', methods=['GET'])
def get_creditos():
    """Obtiene los créditos del usuario"""
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
        })
    finally:
        db.close()

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
        } for m in materias])
    finally:
        db.close()

@auth_bp.route('/inscribirse/<int:materia_id>', methods=['POST'])
def inscribirse_materia(materia_id):
    """Inscribe al usuario en una materia"""
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
        })
    finally:
        db.close()

@auth_bp.route('/mis-materias', methods=['GET'])
def mis_materias():
    """Obtiene las materias en las que está inscrito el usuario"""
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
        
        return jsonify(materias)
    finally:
        db.close()