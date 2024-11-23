from ..DataBase import DataBaseConnectionHelper


class LoginScreenRepository:

    def __init__(self):
        pass

    @staticmethod
    def authenticate_user(login: str, password: str = "null") -> str:
        connection = DataBaseConnectionHelper().connect()
        cursor = connection.cursor()
        cursor.execute(f"select authenticateUser('{login}', {password})")
        status = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return status

    @staticmethod
    def authorize_user(role: str, login: str, password: str = "null") -> tuple:
        roles_commands: dict[str, str] = {"даритель": f"select * from findDonatorWithLoginData('{login}', {password});",
                                          "сотрудник": f"select * from findEmployeeWithLoginData('{login}', {password});"}
        connection = DataBaseConnectionHelper().connect()
        cursor = connection.cursor()
        cursor.execute(roles_commands[role])
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        return user_data

    @staticmethod
    def get_roles() -> list[str]:
        return ["даритель", "сотрудник"]
