import psycopg2

from .GLOBALS import ConnectionStringParams

__all__ = ["DataBaseConnectionHelper"]


class DataBaseConnectionHelper:

    def __init__(self):
        pass

    def connect(self, database_name: str = ConnectionStringParams.DATABASE_NAME,
                user_name: str = ConnectionStringParams.USER,
                password: str = ConnectionStringParams.PASSWORD,
                host: str = ConnectionStringParams.HOST):
        return psycopg2.connect(dbname=database_name, user=user_name, password=password, host=host)
