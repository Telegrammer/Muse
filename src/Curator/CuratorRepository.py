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

    def update_request_status(self, request_id: int, new_status: str):
        self.prepare_command()
        self._cursor.execute(f"call updateRequestStatus({request_id}, '{new_status}')")
        self._connection.commit()

    def count_approved_requests(self):
        self.prepare_command()
        self._cursor.execute("select * from countApprovedRequests()")
        count = self._cursor.fetchone()[0]
        return count

    def add_exhibit(self,
                    exhibit_name: str,
                    exhibit_type: str,
                    hall: str,
                    description: str,
                    exhibit_size: str,
                    creation_year: str,
                    origin: str):
        self.prepare_command()
        if creation_year == '':
            creation_year = 'null'
        if origin == '':
            origin = 'null'

        self._cursor.execute(
            f"call addExhibit('{exhibit_name}',"
            f" '{exhibit_type}', {hall},"
            f" '{description}', '{exhibit_size}',"
            f" {creation_year}, '{origin}')")
        self._connection.commit()

    def get_donator_by_request_id(self, request_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getDonatorByRequestId({request_id})")
        donator_id = self._cursor.fetchone()[0]
        return donator_id

    def add_act(self, donator_id: int):
        self.prepare_command()
        self._cursor.execute(f"call addAct({donator_id})")
        self._connection.commit()

