CREATE TABLE estudiantes_habilitados (
    id SERIAL PRIMARY KEY,
    universidad VARCHAR(255) NOT NULL,
    tipo_documento VARCHAR(10) NOT NULL,
    numero_documento VARCHAR(20) UNIQUE NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    correo_universidad VARCHAR(255) NOT NULL,
    fecha_inicio_habilitacion DATE NOT NULL,
    fecha_fin_habilitacion DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    universidad VARCHAR(255) NOT NULL,
    codigo_universidad VARCHAR(20) UNIQUE,
    numero_documento VARCHAR(20) UNIQUE NOT NULL,
    tipo_documento VARCHAR(10) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    correo_universidad VARCHAR(255) NOT NULL,
    contraseña_hash VARCHAR(255) NOT NULL,
    email_verificado BOOLEAN DEFAULT FALSE,
    token_verificacion VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
CREATE INDEX idx_estudiantes_dni ON estudiantes_habilitados(numero_documento);
CREATE INDEX idx_estudiantes_uni ON estudiantes_habilitados(universidad);
CREATE INDEX idx_usuarios_dni ON usuarios(numero_documento);
SELECT * FROM usuarios
SELECT * FROM estudiantes_habilitados
 