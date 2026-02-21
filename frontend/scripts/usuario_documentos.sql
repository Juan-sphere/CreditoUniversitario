CREATE TYPE tipo_documento_sustento_enum AS ENUM (
    'SUSTENTO_INGRESOS',
    'BOLETAS_HABERES',
    'PDT_SUNAT',
    'REPORTE_TRIBUTARIO_ANUAL',
    'VOUCHER_RUS',
    'REPORTE_TRIBUTARIO_TERCEROS',
    'RECIBOS_HONORARIOS',
    'RECIBO_SERVICIO'
);
 
 CREATE TABLE usuario_documentos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    tipo_documento tipo_documento_sustento_enum NOT NULL,
    nombre_original VARCHAR(255) NOT NULL,
    bucket_name VARCHAR(150) NOT NULL,
    object_name TEXT NOT NULL, 
    url_publica TEXT, 
    mime_type VARCHAR(100),
    size_bytes BIGINT,
    estado VARCHAR(30) DEFAULT 'ACTIVO',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_usuario_documento
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);
 