CREATE TABLE users
(
    rut               VARCHAR(13) PRIMARY KEY,
    name              VARCHAR(50),
    lastname          VARCHAR(50),
    email          VARCHAR(100),
    created_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL,
    updated_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE users IS 'Cuentas de Simpli Route';
COMMENT ON COLUMN users.rut IS 'rut del estudiante';
COMMENT ON COLUMN users.name IS 'Nombre';
COMMENT ON COLUMN users.lastname IS 'Apellido';
COMMENT ON COLUMN users.email IS 'Email';
COMMENT ON COLUMN users.created_in_rds_at IS 'Fecha de creación en la base de datos';
COMMENT ON COLUMN users.updated_in_rds_at IS 'Fecha de actualización en en la base de datos';

-- Inserción de 3 registros de prueba
INSERT INTO users (rut, name, lastname, email, created_in_rds_at)
VALUES 
('12345678-9', 'Juan', 'Pérez', 'juan.perez@email.com', NOW()),
('98765432-1', 'María', 'González', 'maria.gonzalez@email.com', NOW()),
('11223344-5', 'Carlos', 'López', 'carlos.lopez@email.com', NOW());