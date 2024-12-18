import psycopg2.extensions

from ..AbstractRepository import AbstractRepository
from ..DataBase import DataBaseConnectionHelper


class DonatorRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def prepare_command(self):
        self._connection: psycopg2.extensions.connection = DataBaseConnectionHelper().connect()
        self._cursor: psycopg2.extensions.cursor = self._connection.cursor()

    def get_donator_requests(self, donator_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getDonatorRequests({donator_id});")
        donator_requests = self._cursor.fetchall()
        return donator_requests

    @AbstractRepository.handle_database_errors
    def add_request(self, donator_id: int, description: str):
        self.prepare_command()
        description = AbstractRepository.turn_into_non_empty_string(description)
        self._cursor.execute(f"call addRequest({donator_id}, {description})")
        self._connection.commit()

    def get_donator_exhibits(self, donator_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getDonatorExhibits({donator_id})")
        exhibits = self._cursor.fetchall()
        return exhibits

    def get_donator_popular_exhibits(self, donator_id: int):
        self.prepare_command()
        self._cursor.execute(f"select * from getDonatorPopularExhibits({donator_id})")
        exhibits = self._cursor.fetchall()
        return exhibits
