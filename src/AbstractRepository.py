from abc import ABC, abstractmethod

from psycopg2.extensions import connection, cursor


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
    def set_order(base_part: str, function_name: str, attributes: tuple[tuple[str, bool]]):
        command_string = base_part

        if attributes is None:
            return command_string

        if len(attributes) == 0:
            return command_string

        command_string += " order by "
        for name, is_ascending in attributes:
            order_type: str = "asc" if is_ascending is True else "desc"
            command_string += f"{function_name} {order_type}, "

        command_string += "\n"
        command_string = command_string.replace(", \n", ";\n")
        return command_string
