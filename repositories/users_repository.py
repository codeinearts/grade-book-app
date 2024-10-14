from utils.commons.postgres_operations import PostgresConn
from typing import Tuple, ClassVar, List
from utils.commons.users_data_models import User

pos = PostgresConn()

class Repository:
    table_name: ClassVar[str] = "public.users"

    def create(self, user: User) -> str:
        """
        Inserta un nuevo usuario en la base de datos.
        """

        try:
            # Abrir la conexión a la base de datos
            pos.open_connection()

            # Construcción dinámica de la consulta SQL
            query: str = f"""
                INSERT INTO {self.table_name}
                    ({', '.join(user.model_dump().keys())}, created_in_rds_at)
                VALUES
                    ({', '.join(['%s'] * len(user.model_dump()))}, NOW());
            """

            # Obtener los valores del usuario para la inserción
            values: tuple = tuple(user.model_dump().values())

            # Ejecutar la consulta con los valores
            pos.execute_query(query, values)

            # Devolver un mensaje de éxito o el ID del usuario creado
            return "Usuario creado exitosamente"

        except Exception as error:
            # Manejar el error y devolver un mensaje de error
            print(f"Error al insertar los datos: {error}")
            return f"Error al añadir el usuario: {error}"

        finally:
            # Asegurarse de cerrar la conexión a la base de datos
            pos.close_connection()
