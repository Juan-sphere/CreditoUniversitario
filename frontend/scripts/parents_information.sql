CREATE TYPE parent_type_enum AS ENUM (
    'PADRE',
    'MADRE'
);

CREATE TYPE parent_document_type_enum AS ENUM (
    'DNI',
    'CE',
    'PASAPORTE'
);

CREATE TABLE parents_information (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    parent_type parent_type_enum NOT NULL, -- PADRE o MADRE

    -- DATOS GENERALES
    tipo_documento parent_document_type_enum NOT NULL,
    numero_documento VARCHAR(20) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    fecha_nacimiento DATE NOT NULL,
    vive BOOLEAN NOT NULL,
    estado_civil VARCHAR(50) NOT NULL,
    es_conviviente BOOLEAN NOT NULL,

    -- DATOS CONTACTO
    correo_personal VARCHAR(255),
    correo_trabajo VARCHAR(255),
    telefono_celular VARCHAR(20),
    celular_trabajo VARCHAR(20),

    -- DATOS LABORALES
    vive_con_usuario BOOLEAN NOT NULL,
    trabaja BOOLEAN NOT NULL,
    tipo_trabajo VARCHAR(100),
    tiene_empresa BOOLEAN,
    responsable_economia BOOLEAN,
    contribuye_economia BOOLEAN,
    grado_instruccion VARCHAR(100),
    profesion_oficio VARCHAR(150),
    problemas_salud BOOLEAN NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_parent_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_parent_usuario ON parents_information(usuario_id);

CREATE UNIQUE INDEX unique_parent_per_user
ON parents_information(usuario_id, parent_type);