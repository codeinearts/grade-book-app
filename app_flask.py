from flask import Flask, request, redirect, url_for
from psycopg2 import connect, OperationalError

# Crear la conexión
def get_db_connection():
    try:
        conn = connect(
            host="postgres-database",  # Nombre del servicio Docker
            port=5432,
            user="postgres",
            database="postgres",
            password="lagranzanahoriavendra",
        )
        return conn
    except OperationalError as error:
        print(f"Error connecting to the database: {error}")
        return None

app = Flask(__name__)

@app.route('/')
def hello_geek():
    # HTML de bienvenida para el home
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bienvenido a la App de Gestión</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 18px;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenido a la App de Gestión de Estudiantes</h1>
        <p>Esta es la página principal de nuestra aplicación donde puedes gestionar y visualizar datos de los estudiantes.</p>
        <p>Haz clic en el enlace de abajo para ver la lista de correos electrónicos de los estudiantes registrados.</p>
        <a href="/list-email-students">Ver lista de correos electrónicos</a><br><br>
        <a href="/add-student">Añadir nuevo estudiante</a>
    </body>
    </html>
    """
    return html_content

@app.route('/list-email-students')
def read_email():
    conn = get_db_connection()
    if not conn:
        return "<h1>Database connection error!</h1>"

    cursor = conn.cursor()
    try:
        email_list = []
        query = "SELECT * FROM students;"
        cursor.execute(query)

        # Obtener nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]
        column_positions = {name: idx for idx, name in enumerate(column_names)}

        for name, idx in column_positions.items():
            if name == "email":
                email_col_idx = idx

        records = cursor.fetchall()
        for row in records:
            email_list.append(row[email_col_idx])

        # Crear la lista HTML
        email_items = ''.join(f"<li>{email}</li>" for email in email_list)
        html_content = f"""
        <h1>Lista de correos electrónicos</h1>
        <ul>
            {email_items}
        </ul>
        """
        return html_content

    except Exception as error:
        print(f"Error fetching data: {error}")
        return f"ups error! {error}"

    finally:
        cursor.close()
        conn.close()

# Ruta para añadir un estudiante
@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Recoger los datos del formulario
        rut = request.form['rut']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']

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

    # Si es una petición GET, mostramos el formulario
    html_content = """
    <h1>Añadir nuevo estudiante</h1>
    <form method="POST" action="/add-student">
        <label for="rut">RUT:</label><br>
        <input type="text" id="rut" name="rut"><br><br>
        <label for="name">Nombre:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <label for="lastname">Apellido:</label><br>
        <input type="text" id="lastname" name="lastname"><br><br>
        <label for="email">Correo electrónico:</label><br>
        <input type="email" id="email" name="email"><br><br>
        <input type="submit" value="Añadir Estudiante">
    </form>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
