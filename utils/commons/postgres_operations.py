from psycopg2 import connect, OperationalError
from typing import Tuple, Any, Union
from psycopg2.errors import ForeignKeyViolation


class PostgresConn:
    def __init__(self) -> None:
        print("initialize connection to database")

    def open_connection(self) -> Union[None, str]:
        """
        TODO: agregar docstirng
        """
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

    def execute_query(self, query: str, values: tuple, retry: int = 0) -> None:
        """
        Intenta ejecutar una query a la base de datos.
        :param query: Consulta SQL.
        :param values: Valores a sustituir en la query.
        :param retry: Número de reintentos.
        """
        query_succeeded: bool = self.__try_query(query, values)
        # TODO: validar si utilizar retry
        if query_succeeded:
            print("operation successfully...")
        else:
            print("error operation...")

    def __try_query(self, query: str, values: tuple) -> bool:
        """
        Intenta ejecutar una query en la base de datos.
        :param query: Consulta SQL.
        :param values: Valores a sustituir en la query.
        :return: ¿Éxito en la operación?
        """
        success: bool = False
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query, values)
            success = True

        except ForeignKeyViolation as error:
            message: str = "Foreign Key Violation, "
            message += f"registro será enviado a reintento. Detalle: {error}"
            print(message)
            self.connection.rollback()

        finally:
            self.connection.commit()
            self.cursor.close()

        return success


