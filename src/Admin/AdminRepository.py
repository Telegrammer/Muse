from enum import IntEnum

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


class AdminRepository:

    def __init__(self):
        self.__connection = property()
        self.__cursor = property()

    def prepare_command(self):
        self.__connection = DataBaseConnectionHelper().connect()
        self.__cursor = self.__connection.cursor()

    def get_employees(self, sender_phone_number: str, row_range_start: int = -1, row_range_end: int = -1) -> list:
        self.prepare_command()
        self.__cursor.execute(
            f"select * from getEmployees('{sender_phone_number}', {row_range_start}, {row_range_end});")
        employees = self.__cursor.fetchall()

        for i in range(len(employees)):
            employees[i] = list(employees[i])
            employees[i][EmployeeData.birthDate] = employees[i][EmployeeData.birthDate].strftime("%d.%m.%Y")

        return employees

    def get_employees_positions(self):
        self.prepare_command()
        self.__cursor.execute(f"select * from getEmployeesPositions()")
        positions = self.__cursor.fetchall()
        positions = [position[0] for position in positions]
        return positions

    def get_exhibits(self, row_range_start: int = -1, row_range_end: int = -1) -> list:
        self.prepare_command()
        self.__cursor.execute(f"select * from getExhibits({row_range_start}, {row_range_end});")
        exhibits = self.__cursor.fetchall()

        return exhibits

    def get_exhibit_types(self):
        self.prepare_command()
        self.__cursor.execute(f"select * from getExhibitTypes();")
        exhibit_types = [exhibitType[0] for exhibitType in self.__cursor.fetchall()]

        return exhibit_types

    def get_exhibit_halls(self):
        self.prepare_command()
        self.__cursor.execute(f"select * from getExhibitHalls();")
        exhibit_halls = [exhibitHall[0] for exhibitHall in self.__cursor.fetchall()]

        return exhibit_halls

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()
