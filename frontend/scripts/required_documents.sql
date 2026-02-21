CREATE TABLE required_documents (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    -- Tipo de documento (flexible)
    tipo_documento VARCHAR(150) NOT NULL,

    -- Metadata del archivo en Cloud Storage
    bucket_name VARCHAR(150) NOT NULL,
    object_name TEXT NOT NULL,              -- ruta dentro del bucket
    nombre_original VARCHAR(255) NOT NULL,
    mime_type VARCHAR(100),
    size_bytes BIGINT,

    -- Control interno
    estado VARCHAR(30) DEFAULT 'PENDIENTE', -- PENDIENTE, VALIDADO, OBSERVADO
    observaciones TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_required_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);