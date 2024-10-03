from psycopg2 import connect, OperationalError
from typing import Tuple, Any, Union


class PostgresConn:
    def __init__(self) -> None:
        print("initialize connection to database")

    def open_connection(self) -> Union[None, str]:
        try:
            self.connection = connect(
                host="postgres-database",  # Nombre del servicio Docker
                port=5432,
                user="postgres",
                database="postgres",
                password="lagranzanahoriavendra",
            )
            print(f"conn: {self.connection}")
            print("connection successfully...")
            return self.connection
        except OperationalError as error:
            print(f"Error connecting to the database: {error}")
            return f"Error connecting to the database: {error}"

    def close_connection(self) -> None:
        """
        Cierra la conexión de comunicación a la base de datos.
        """
        self.connection.close()
