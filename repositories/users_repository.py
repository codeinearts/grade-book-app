from utils.commons.postgres_operations import PostgresConn
from typing import Tuple, ClassVar, List


class Repository:
    table_name: ClassVar[str] = "public.users"

    def __init__(self):
        self.pc = PostgresConn()

    def create(self, user) -> str:
        self.pc.open_connection()
        query: str = f"""
            INSERT INTO {self.table_name}
                (rut, name, lastname, email, created_in_rds_at)
            VALUES
            (%s, %s, %s, %s, NOW())
            """



