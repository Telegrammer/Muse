import psycopg2

import GLOBALS

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname=GLOBALS.ConnectionStringParams.DATABASE_NAME,
                            user=GLOBALS.ConnectionStringParams.USER,
                            password=GLOBALS.ConnectionStringParams.password,
                            host=GLOBALS.ConnectionStringParams.host)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Сотрудник')
    all_users = cursor.fetchall()
    print(all_users)
    cursor.close()  # закрываем курсор
    conn.close()
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')


class DataBaseConnectionHelper:

    def __init__(self):
        self.__data_base = property()

    def connect(self, server: str, database_name: str, user_name: str, password: str):
        if self.__data_base is None:
            pass
