from abc import ABC, abstractmethod
from typing import Callable

from PyQt5.QtWidgets import QMessageBox
from psycopg2.errors import RaiseException, DatabaseError
from psycopg2.extensions import connection, cursor


class AlertMessageBox(QMessageBox):

    def __init__(self, parent=None, title: str = 'Информация', body: str = ''):
        QMessageBox.__init__(self, parent)
        self.setWindowTitle(title)
        self.setText(body)
        self.setModal(True)
        self.exec_()


class AbstractRepository(ABC):

    def __init__(self):
        self._connection: connection = property()
        self._cursor: cursor = property()

    @abstractmethod
    def prepare_command(self):
        pass

    def __del__(self):
        self._cursor.close()
        self._connection.close()

    @staticmethod
    def handle_database_errors(command: Callable):
        def wrapper(*args, **kwargs):
            try:
                command(*args, **kwargs)
            except RaiseException as exception:
                exception_string = str(exception)
                exception_string = exception_string[exception_string.find(' ') + 1:exception_string.find('CONTEXT')]
                AlertMessageBox(title='Исключение', body=exception_string)
            except DatabaseError as error:
                error_string = str(error)
                error_string = error_string.replace('_', ' ')
                error_string = error_string[:error_string.find("DETAIL")]
                if "не умещается" in error_string:
                    error_string = 'Превышано максимальное количество символов'
                AlertMessageBox(title='Ошибка базы данных', body=error_string)

        return wrapper

    @staticmethod
    def build_filters(base_part: str, function_name: str, attributes: tuple[tuple[str, str]]) -> str:
        command_string = base_part
        if attributes is not None and (len(attributes)) != 0:
            command_string += " where "
            for name, value in attributes:
                command_string += f"{function_name}.{name} {value} and "

        command_string += "\n"
        command_string = command_string.replace("and \n", ";")
        return command_string

    @staticmethod
    def turn_into_non_empty_string(database_string_argument: str):
        if database_string_argument == '':
            return 'null'
        return f"""'{database_string_argument}'"""

    @staticmethod
    def convert_to_int_string(database_int_argument):
        try:
            return f"{int(database_int_argument)}"
        except ValueError:
            return "null"

    @staticmethod
    def convert_to_float_string(database_float_argument):
        try:
            return f"{round(float(database_float_argument), 2)}"
        except ValueError:
            return "null"

    @staticmethod
    def set_order(base_part: str, function_name: str, attributes: tuple[tuple[str, bool]]):
        command_string = base_part

        if attributes is None:
            return command_string

        if len(attributes) == 0:
            return command_string

        command_string += " order by "
        for name, is_ascending in attributes:
            order_type: str = "asc" if is_ascending is True else "desc"
            command_string += f"{function_name}.{name} {order_type}, "

        command_string += "\n"
        command_string = command_string.replace(", \n", ";\n")
        return command_string
