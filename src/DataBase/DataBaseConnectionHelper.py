class DataBaseConnectionHelper:

    def __init__(self):
        self.__data_base = property()

    def connect(self, server: str, database_name: str, user_name: str, password: str):
        if self.__data_base is None:
            pass
