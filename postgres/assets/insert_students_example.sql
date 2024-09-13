-- Inserción de 3 registros de prueba
INSERT INTO users (rut, name, lastname, email, created_in_rds_at)
VALUES 
('12345678-9', 'Juan', 'Pérez', 'juan.perez@email.com', NOW()),
('98765432-1', 'María', 'González', 'maria.gonzalez@email.com', NOW()),
('11223344-5', 'Carlos', 'López', 'carlos.lopez@email.com', NOW());