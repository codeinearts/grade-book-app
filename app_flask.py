from flask import Flask
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
        return f"Error connecting to the database: {error}"

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return "<h1>Yamete kudasai</h1>"  # Etiqueta cerrada correctamente


@app.route('/read-email')
def read_email():
    conn = get_db_connection()
    if not conn:
        return "<h1>Database connection error!</h1>"

    cursor = conn.cursor()
    try:
        msg = ""
        email_list = []
        query = "SELECT * FROM users;"
        cursor.execute(query)

        print("cursor.description")
        print(cursor.description)
        # Obtener nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]
        column_positions = {name: idx for idx, name in enumerate(column_names)}

        # Imprimir nombres de columnas y su posición
        print("Columnas y posiciones:")
        for name, idx in column_positions.items():
            print(f"Columna: {name}, Posición: {idx}")
            if name == "email":
                email_col_idx = idx

        records = cursor.fetchall()
        for row in records:
            print(type(row))
            print(row)
            email_list.append(row[email_col_idx])  # Asumiendo que el email está en la segunda columna

        msg = ' '.join(email_list)

        html_content = f"""
        <h1>{msg}</h1>
        """
        return html_content

    except Exception as error:
        print(f"Error fetching data: {error}")
        return f"ups error! {error}"

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
