from utils.commons.postgress_connection import PostgresConn

class Repository:
    def __init__(self):
        self.pc = PostgresConn()

    def create(self) -> str:
        query = "INSERT INTO students (rut, name, lastname, email, created_in_rds_at) VALUES (%s, %s, %s, %s, NOW())"
        return query


