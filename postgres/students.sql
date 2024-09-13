CREATE TABLE students
(
    rut               VARCHAR(13) PRIMARY KEY,
    name              VARCHAR(50),
    lastname          VARCHAR(50),
    email          VARCHAR(100),
    created_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL,
    updated_in_rds_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE students IS 'Cuentas de Simpli Route';
COMMENT ON COLUMN students.rut IS 'rut del estudiante';
COMMENT ON COLUMN students.name IS 'Nombre';
COMMENT ON COLUMN students.lastname IS 'Apellido';
COMMENT ON COLUMN students.email IS 'Email';
COMMENT ON COLUMN students.created_in_rds_at IS 'Fecha de creación en la base de datos';
COMMENT ON COLUMN students.updated_in_rds_at IS 'Fecha de actualización en en la base de datos';
