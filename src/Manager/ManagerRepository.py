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
        excursions = self._cursor.fetchall()
        return excursions

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

    @AbstractRepository.handle_database_errors
    def add_hall_to_excursion(self, excursion_id: int, hall_id: int):
        self.prepare_command()
        self._cursor.execute(f"call addHallToExcursion({excursion_id}, {hall_id});")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def add_halls_to_excursion(self, excursion_id: int, halls: list[int]):
        self.prepare_command()
        for hall in halls:
            self._cursor.execute(f"call addHallToExcursion({excursion_id}, {hall});")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def remove_hall_from_excursion(self, excursion_id: int, hall_id: int):
        self.prepare_command()
        self._cursor.execute(f"call removeHallFromExcursion({excursion_id}, {hall_id});")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
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

    @AbstractRepository.handle_database_errors
    def add_excursion(self, excursion_name: str, employee_contacts: str, description: str, amount: str):
        self.prepare_command()
        excursion_name = AbstractRepository.turn_into_non_empty_string(excursion_name)
        description = AbstractRepository.turn_into_non_empty_string(description)
        amount = AbstractRepository.convert_to_float_string(amount)
        self._cursor.execute(f"call addExcursion({excursion_name}, '{employee_contacts}', {description}, {amount})")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def remove_excursion(self, excursion_id: int):
        self.prepare_command()
        self._cursor.execute(f"call removeExcursion({excursion_id});")
        self._connection.commit()

    def get_exhibitions(self, employee_id: int, row_range_start: int = -1, row_range_end: int = -1):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitions({employee_id}, {row_range_start}, {row_range_end});")
        exhibitions = self._cursor.fetchall()
        return exhibitions

    def find_available_exhibits(self, exhibition_id: int, filters: tuple[tuple[str, str]] = None):
        self.prepare_command()
        connection_string = f"select * from getAvailableExhibits({exhibition_id})"
        connection_string = self.build_filters(connection_string, "getAvailableExhibits", filters)
        self._cursor.execute(connection_string)
        exhibits = self._cursor.fetchall()
        return exhibits

    def get_exhibition_composition(self, exhibition_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitionComposition({exhibition_id})")
        exhibits = self._cursor.fetchall()
        return exhibits

    @AbstractRepository.handle_database_errors
    def add_exhibit_to_exhibition(self, exhibition_id: int, exhibit_id: int):
        self.prepare_command()
        self._cursor.execute(f"call addExhibitToExhibition({exhibition_id}, {exhibit_id});")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def add_exhibits_to_exhibitions(self, exhibition_id: int, exhibits: list[int]):
        self.prepare_command()
        for exhibit in exhibits:
            self._cursor.execute(f"call addExhibitToExhibition({exhibition_id}, {exhibit});")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def remove_exhibit_from_exhibition(self, exhibition_id: int, exhibit_id: int):
        self.prepare_command()
        self._cursor.execute(f" call removeExhibitFromExhibition({exhibition_id}, {exhibit_id})")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def add_exhibition(self, employee_id: int, name: str, description: str, size: str, start_date: str, end_date: str):
        self.prepare_command()
        name = AbstractRepository.turn_into_non_empty_string(name)
        description = AbstractRepository.turn_into_non_empty_string(description)
        size = AbstractRepository.convert_to_float_string(size)
        self._cursor.execute(
            f" call addExhibition({employee_id}, {name}, {description}, {size}, '{start_date}', '{end_date}')")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def remove_exhibition(self, exhibition_id: int):
        self.prepare_command()
        self._cursor.execute(
            f" call removeExhibition({exhibition_id})")
        self._connection.commit()

    @AbstractRepository.handle_database_errors
    def edit_exhibition(self, exhibition_id: int, exhibition_name: str, description: str, size: str, start_date: str,
                        end_date: str):
        self.prepare_command()
        exhibition_name = AbstractRepository.turn_into_non_empty_string(exhibition_name)
        description = AbstractRepository.turn_into_non_empty_string(description)
        size = AbstractRepository.convert_to_float_string(size)

        self._cursor.execute(
            f"call editExhibition({exhibition_id}, {exhibition_name}, {description}, {size}, '{start_date}', '{end_date}')")
        self._connection.commit()

    def find_exhibitions(self, employee_id: int, row_range_start: int = -1, row_range_end: int = -1,
                         filters: tuple[tuple[str, str]] = None, orders: tuple[tuple[str, bool]] = None):
        self.prepare_command()
        command_string = f"select * from getManagerExhibitions({employee_id}, {row_range_start}, {row_range_end})"
        command_string = self.build_filters(command_string, "getManagerExhibitions", attributes=filters)
        command_string = self.set_order(command_string, "getManagerExhibitions", orders)
        self._cursor.execute(command_string)
        exhibitions = self._cursor.fetchall()
        return exhibitions

    def get_exhibition_calendar_info(self):
        self.prepare_command()
        self._cursor.execute("select * from getExhibitionCalendarInfo()")
        exhibitions = self._cursor.fetchall()
        return exhibitions

    def find_all_exhibitions(self, employee_id: int,
                             filters: tuple[tuple[str, str]] = None, orders: tuple[tuple[str, bool]] = None):
        self.prepare_command()
        command_string = f"select * from getAllExhibitions({employee_id})"
        command_string = self.build_filters(command_string, "getAllExhibitions", attributes=filters)
        command_string = self.set_order(command_string, "getAllExhibitions", orders)
        self._cursor.execute(command_string)
        exhibitions = self._cursor.fetchall()
        return exhibitions

    def identify_popular_exhibits(self, exhibit_count: int = 10):
        self.prepare_command()
        self._cursor.execute(f"select * from identifymostpopularexhibits({exhibit_count})")
        exhibits = self._cursor.fetchall()
        return exhibits
