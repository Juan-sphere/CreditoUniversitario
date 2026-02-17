from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.auth.routes import auth_bp
from app.db.database import engine, Base
from app.db.models import Usuario, Creditos, Materia, Inscripcion

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Habilitar CORS
    CORS(app)
    
    # Crear tablas
    Base.metadata.create_all(bind=engine)
    
    # Registrar blueprints
    app.register_blueprint(auth_bp)
    
    # Ruta de prueba
    @app.route('/')
    def index():
        return {
            'mensaje': 'API de Sistema de Crédito Universitario',
            'version': '1.0',
            'endpoints': {
                'auth': '/auth',
                'login': 'POST /auth/login',
                'registro': 'POST /auth/registro',
                'logout': 'POST /auth/logout',
                'me': 'GET /auth/me',
                'creditos': 'GET /auth/creditos',
                'materias': 'GET /auth/materias',
                'inscribirse': 'POST /auth/inscribirse/<id>',
                'mis_materias': 'GET /auth/mis-materias'
            }
        }
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Ruta no encontrada'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Error interno del servidor'}, 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)