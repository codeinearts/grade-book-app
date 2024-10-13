from repositories.users_repository import Repository
from flask import render_template

in_construction: str = "in-construction.html"

class Service:
    def __init__(self):
        self.repository = Repository()

    def create(self, user: dict) -> str:

        # Recoger los datos del formulario
        rut = user.get('rut')
        name = user.get('name')
        lastname = user.get('lastname')
        email = user.get('email')

        # Validar los campos básicos
        if not rut or not name or not lastname or not email:
            return "<h1>Faltan datos. Por favor, rellena todos los campos.</h1>"

        # Conectar a la base de datos e insertar el nuevo estudiante
        conn = get_db_connection()
        if not conn:
            return "<h1>Error de conexión a la base de datos.</h1>"
        
        cursor = conn.cursor()
        try:
            query = "INSERT INTO students (rut, name, lastname, email, created_in_rds_at) VALUES (%s, %s, %s, %s, NOW())"
            cursor.execute(query, (rut, name, lastname, email))
            conn.commit()
            return redirect(url_for('hello_geek'))

        except Exception as error:
            print(f"Error inserting data: {error}")
            return f"<h1>Error al añadir el estudiante: {error}</h1>"

        finally:
            cursor.close()
            conn.close()

    def read(self) -> str:
        return render_template(in_construction)
