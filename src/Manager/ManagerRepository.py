from enum import IntEnum

import psycopg2.extensions

from ..AbstractRepository import AbstractRepository
from ..DataBase import DataBaseConnectionHelper


class ManagerRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def prepare_command(self):
        self._connection: psycopg2.extensions.connection = DataBaseConnectionHelper().connect()
        self._cursor: psycopg2.extensions.cursor = self._connection.cursor()

    def get_excursions(self, row_range_start: int = -1, row_range_end: int = -1):
        self.prepare_command()
        self._cursor.execute(f"select * from getExcursions({row_range_start}, {row_range_end})")
        excursions = self._cursor.fetchall()
        return excursions

    def find_excursions(self, row_range_start: int = -1, row_range_end: int = -1,
                        filters: tuple[tuple[str, str]] = None, orders: tuple[tuple[str, bool]] = None):
        self.prepare_command()
        command_string = f"select * from getExcursions({row_range_start}, {row_range_end})"
        command_string = self.build_filters(command_string, "getExcursions", attributes=filters)
        command_string = self.set_order(command_string, "getExcursions", orders)
        self._cursor.execute(command_string)
        exhibits = self._cursor.fetchall()
        return exhibits

    def get_guides(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getGuides();")
        guides = self._cursor.fetchall()
        return [guide[0] for guide in guides]

    def find_available_halls(self, excursion_id: int, filters: tuple[tuple[str, str]] = None):
        self.prepare_command()
        connection_string = f"select * from getAvailableHalls({excursion_id})"
        connection_string = self.build_filters(connection_string, "getAvailableHalls", filters)
        self._cursor.execute(connection_string)
        halls = self._cursor.fetchall()
        return halls

    def get_excursion_halls(self, excursion_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getExcursionHalls({excursion_id})")
        halls = self._cursor.fetchall()
        return halls

    def add_hall_to_excursion(self, excursion_id: int, hall_id: int):
        self.prepare_command()
        self._cursor.execute(f"call addHallToExcursion({excursion_id}, {hall_id});")
        self._connection.commit()

    def add_halls_to_excursion(self, excursion_id: int, halls: list[int]):
        self.prepare_command()
        for hall in halls:
            self._cursor.execute(f"call addHallToExcursion({excursion_id}, {hall});")
        self._connection.commit()

    def remove_hall_from_excursion(self, excursion_id: int, hall_id: int):
        self.prepare_command()
        self._cursor.execute(f"call removeHallFromExcursion({excursion_id}, {hall_id});")
        self._connection.commit()

    def edit_excursion(self, attributes: list[tuple[str, IntEnum]], excursion_id: int):
        self.prepare_command()
        command_string: str = f"call editExcursion({excursion_id}, "

        for value, attribute_type in attributes:
            if value == "":
                command_string += "null, "
                continue
            try:
                command_string += f"{float(value)}"
            except ValueError:
                command_string += f"'{value}'"
            command_string += ', '

        command_string += '\n'
        command_string = command_string.replace(", \n", "")
        command_string += ");"

        self._cursor.execute(command_string)
        self._connection.commit()

    def add_excursion(self, excursion_name: str, employee_contacts: str, description: str, amount: str):
        self.prepare_command()
        self._cursor.execute(f"call addExcursion('{excursion_name}', '{employee_contacts}', '{description}', {amount})")
        self._connection.commit()

    def remove_excursion(self, excursion_id: int):
        self.prepare_command()
        self._cursor.execute(f"call removeExcursion({excursion_id});")
        self._connection.commit()

    def get_exhibitions(self, employee_id: int, row_range_start: int = -1, row_range_end: int = -1):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitions({employee_id}, {row_range_start}, {row_range_end});")
        exhibitions = self._cursor.fetchall()
        return exhibitions
