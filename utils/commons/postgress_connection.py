from psycopg2 import connect, OperationalError


class PostgresConn:
    def __init__(self) -> None:
        pass
        print("initialize connection to database")

    def open_conn():
        try:
            conn = connect(
                host="postgres-database",  # Nombre del servicio Docker
                port=5432,
                user="postgres",
                database="postgres",
                password="lagranzanahoriavendra",
            )
            print(f"conn: {conn}")
            print("connection successfully...")
            return conn
        except OperationalError as error:
            print(f"Error connecting to the database: {error}")
            return f"Error connecting to the database: {error}"
        
    def close_conn():
        pass