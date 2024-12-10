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