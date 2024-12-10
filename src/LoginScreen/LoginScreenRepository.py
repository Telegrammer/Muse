from ..AbstractRepository import AbstractRepository
from ..DataBase import DataBaseConnectionHelper


class LoginScreenRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def prepare_command(self):
        self._connection = DataBaseConnectionHelper().connect()
        self._cursor = self._connection.cursor()

    def authenticate_user(self, login: str, password="null") -> str:
        self.prepare_command()
        self._cursor.execute(f"select authenticateUser('{login}', {password})")
        status = self._cursor.fetchone()[0]
        return status

    def authorize_user(self, role: str, login: str, password="null") -> tuple:
        self.prepare_command()
        roles_commands: dict[str, str] = {
            "даритель": f"select * from findDonatorWithLoginData('{login}', {password});",
            "сотрудник": f"select * from findEmployeeWithLoginData('{login}', {password});"}
        self._cursor.execute(roles_commands[role])
        user_data = self._cursor.fetchone()
        return user_data

    @staticmethod
    def get_roles() -> list[str]:
        return ["даритель", "сотрудник"]
