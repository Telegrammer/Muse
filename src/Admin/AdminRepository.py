from enum import IntEnum

import psycopg2.extensions

from ..AbstractRepository import AbstractRepository
from ..DataBase import DataBaseConnectionHelper


class EmployeeData(IntEnum):
    fullname = 0,
    position = 1,
    birthDate = 2,
    phoneNumber = 3


class ExhibitData(IntEnum):
    name = 0,
    exhibitType = 1,
    hall = 2,
    description = 3,
    size = 4,
    yearOfCreation = 5,
    origin = 6


class AdminRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def prepare_command(self):
        self._connection: psycopg2.extensions.connection = DataBaseConnectionHelper().connect()
        self._cursor: psycopg2.extensions.cursor = self._connection.cursor()

    def get_employees(self, sender_phone_number: str, row_range_start: int = -1, row_range_end: int = -1) -> list:
        self.prepare_command()
        self._cursor.execute(
            f"select * from getEmployees('{sender_phone_number}', {row_range_start}, {row_range_end});")
        employees = self._cursor.fetchall()

        for i in range(len(employees)):
            employees[i] = list(employees[i])
            employees[i][EmployeeData.birthDate + 1] = employees[i][EmployeeData.birthDate + 1].strftime("%d.%m.%Y")

        return employees

    def get_employees_positions(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getEmployeesPositions()")
        positions = self._cursor.fetchall()
        positions = [position[0] for position in positions]
        return positions

    def get_exhibits(self, row_range_start: int = -1, row_range_end: int = -1) -> list:
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibits({row_range_start}, {row_range_end});")
        exhibits = self._cursor.fetchall()

        return exhibits

    def get_exhibit_types(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitTypes();")
        exhibit_types = [exhibitType[0] for exhibitType in self._cursor.fetchall()]

        return exhibit_types

    def get_exhibit_halls(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitHalls();")
        exhibit_halls = [exhibitHall[0] for exhibitHall in self._cursor.fetchall()]

        return exhibit_halls

    def add_employee(self, full_name: str, position: str, birthdate: str, phone_number: str) -> None:
        self.prepare_command()
        self._cursor.execute(
            f"call addEmployee('{full_name}', '{position}', '{birthdate}', '{phone_number}');")
        self._connection.commit()

    def edit_employee(self, new_name: str, new_position: str, new_birth_date: str, new_phone: str, employee_id: str):
        print(new_name, new_position, new_birth_date, new_phone, employee_id)
        self.prepare_command()
        self._cursor.execute(
            f"call editEmployee('{new_name}', '{new_position}', '{new_birth_date}', '{new_phone}', {employee_id});")
        self._connection.commit()

    def remove_employee(self, employee_id: int):
        self.prepare_command()
        self._cursor.execute(
            f"call removeEmployee({employee_id});"
        )
        self._connection.commit()

    def edit_exhibit(self, attributes: list[tuple[str, IntEnum]], exhibit_id: int):
        self.prepare_command()
        command_string: str = "call editExhibit("

        for value, attribute_type in attributes:
            if value == "":
                command_string += "null, "
                continue
            try:
                command_string += f"{int(value)}"
            except ValueError:
                command_string += f"'{value}'"
            command_string += ', '

        command_string += f"{exhibit_id});"

        self._cursor.execute(command_string)
        self._connection.commit()

    def get_exhibit_statuses(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitStatuses();")
        exhibit_statuses = [exhibitStatus[0] for exhibitStatus in self._cursor.fetchall()]

        return exhibit_statuses

    def find_employees(self, sender_phone_number: str, row_range_start: int = -1, row_range_end: int = -1,
                       attributes: tuple[tuple[str, str]] = None, orders: tuple[tuple[str, bool]] = None):
        self.prepare_command()
        command_string: str = f"select * from getEmployees('{sender_phone_number}', {row_range_start}, {row_range_end})"
        command_string = self.build_filters(command_string, "getEmployees", attributes=attributes)
        command_string = self.set_order(command_string, "getEmployees", orders)
        print(command_string)
        self._cursor.execute(command_string)
        employees = self._cursor.fetchall()

        return employees

    def find_exhibits(self, row_range_start: int = -1, row_range_end: int = -1,
                      attributes: tuple[tuple[str, str]] = None, orders: tuple[tuple[str, bool]] = None):
        self.prepare_command()
        command_string = f"select * from getExhibits({row_range_start}, {row_range_end})"
        command_string = self.build_filters(command_string, "getExhibits", attributes=attributes)
        self._cursor.execute(command_string)
        exhibits = self._cursor.fetchall()
        return exhibits