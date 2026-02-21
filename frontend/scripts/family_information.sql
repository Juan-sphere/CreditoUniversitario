CREATE TABLE family_information (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    -- DATOS GENERALES
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),

    parentesco VARCHAR(100) NOT NULL, 

    depende_economicamente BOOLEAN NOT NULL,
    edad INTEGER NOT NULL CHECK (edad >= 0),
    estudia BOOLEAN NOT NULL,
    trabaja BOOLEAN NOT NULL,
    tipo_trabajo VARCHAR(100),
    tiene_empresa BOOLEAN DEFAULT FALSE,

    -- DATOS LABORALES Y ACADÉMICOS
    contribuye_economia BOOLEAN NOT NULL,
    grado_instruccion VARCHAR(100) NOT NULL,
    profesion_oficio VARCHAR(150),
    problemas_salud BOOLEAN NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_family_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);