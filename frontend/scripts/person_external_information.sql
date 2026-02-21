CREATE TABLE person_external_information (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    -- DATOS GENERALES
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),

    parentesco_relacion VARCHAR(150) NOT NULL,

    edad INTEGER NOT NULL CHECK (edad >= 0),

    trabaja BOOLEAN NOT NULL,
    tipo_trabajo VARCHAR(150),

    -- DATOS LABORALES Y ACADÉMICOS
    grado_instruccion VARCHAR(150) NOT NULL,
    profesion_oficio VARCHAR(150),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_external_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE,

    -- Si no trabaja, no debe tener tipo_trabajo
    CONSTRAINT check_trabajo_tipo
        CHECK (
            (trabaja = FALSE AND tipo_trabajo IS NULL)
            OR
            (trabaja = TRUE AND tipo_trabajo IS NOT NULL)
        )
);