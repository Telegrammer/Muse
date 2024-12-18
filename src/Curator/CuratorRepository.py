import psycopg2.extensions

from ..AbstractRepository import AbstractRepository
from ..DataBase import DataBaseConnectionHelper


class CuratorRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def prepare_command(self):
        self._connection: psycopg2.extensions.connection = DataBaseConnectionHelper().connect()
        self._cursor: psycopg2.extensions.cursor = self._connection.cursor()

    def get_donation_acts(self):
        self.prepare_command()
        self._cursor.execute("select * from getDonationActs()")

        donation_acts = self._cursor.fetchall()
        return donation_acts

    def find_donation_acts(self, filters=None):
        self.prepare_command()
        command_string = "select * from getDonationActs()"
        command_string = self.build_filters(command_string, 'getDonationActs', filters)
        self._cursor.execute(command_string)
        donation_acts = self._cursor.fetchall()
        return donation_acts

    def get_exhibit_types(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitTypes();")
        exhibit_types = [exhibitType[0] for exhibitType in self._cursor.fetchall()]

        return exhibit_types

    def get_exhibit_halls(self):
        self.prepare_command()
        self._cursor.execute(f"select * from getExhibitHallsIds();")
        exhibit_halls = [exhibitHall[0] for exhibitHall in self._cursor.fetchall()]

        return exhibit_halls

    def count_unchecked_requests(self):
        self.prepare_command()
        self._cursor.execute(f"select * from countUncheckedRequests()")
        count = self._cursor.fetchone()[0]
        return count

    def find_unchecked_requests(self):
        self.prepare_command()
        self._cursor.execute(f"select * from findUncheckedRequests()")
        requests = self._cursor.fetchall()
        return requests

    def find_approved_requests(self):
        self.prepare_command()
        self._cursor.execute(f"select * from findApprovedRequests()")
        requests = self._cursor.fetchall()
        return requests

    @AbstractRepository.handle_database_errors
    def update_request_status(self, request_id: int, new_status: str):
        self.prepare_command()
        self._cursor.execute(f"call updateRequestStatus({request_id}, '{new_status}')")
        self._connection.commit()

    def count_approved_requests(self):
        self.prepare_command()
        self._cursor.execute("select * from countApprovedRequests()")
        count = self._cursor.fetchone()[0]
        return count

    @AbstractRepository.handle_database_errors
    def add_exhibit(self,
                    exhibit_name: str,
                    exhibit_type: str,
                    hall: str,
                    description: str,
                    exhibit_size: str,
                    creation_year: str,
                    origin: str):
        self.prepare_command()
        exhibit_name = AbstractRepository.turn_into_non_empty_string(exhibit_name)
        exhibit_type = AbstractRepository.turn_into_non_empty_string(exhibit_type)
        hall = AbstractRepository.convert_to_int_string(hall)
        creation_year = AbstractRepository.turn_into_non_empty_string(creation_year)
        origin = AbstractRepository.turn_into_non_empty_string(origin)
        exhibit_size = AbstractRepository.convert_to_float_string(exhibit_size)
        creation_year = AbstractRepository.convert_to_int_string(creation_year)

        self._cursor.execute(
            f"call addExhibit({exhibit_name},"
            f" {exhibit_type}, {hall},"
            f" {description}, {exhibit_size},"
            f" {creation_year}, {origin})")
        self._connection.commit()

    def get_donator_by_request_id(self, request_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getDonatorByRequestId({request_id})")
        donator_id = self._cursor.fetchone()[0]
        return donator_id

    @AbstractRepository.handle_database_errors
    def add_act(self, donator_id: int):
        if donator_id is None:
            return
        self.prepare_command()
        self._cursor.execute(f"call addAct({donator_id})")
        self._connection.commit()
