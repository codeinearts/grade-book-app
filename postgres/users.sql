CREATE TABLE users
(
    hashed_user_rut   VARCHAR(245) PRIMARY KEY,
    rut               VARCHAR(13),
    name              VARCHAR(50),
    lastname          VARCHAR(50),
    email             VARCHAR(100),
    created_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL,
    updated_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE users IS 'Cuentas de usuarios almacenadas';
COMMENT ON COLUMN users.hashed_user_rut IS 'rut del usuario anonimizado';
COMMENT ON COLUMN users.rut IS 'rut del usuario';
COMMENT ON COLUMN users.name IS 'Nombre';
COMMENT ON COLUMN users.lastname IS 'Apellido';
COMMENT ON COLUMN users.email IS 'Email';
COMMENT ON COLUMN users.created_in_rds_at IS 'Fecha de creación en la base de datos';
COMMENT ON COLUMN users.updated_in_rds_at IS 'Fecha de actualización en en la base de datos';
