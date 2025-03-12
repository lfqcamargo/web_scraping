from ...interfaces.logs_repository_interface import LogsRepositoryInterface
from ..settings.connection_handler import DBConnectionHandler


class LogsRepository(LogsRepositoryInterface):
    """
    Concrete implementation of the LogsRepositoryInterface.

    This class handles the interaction with the database for saving logs.
    It uses the provided DBConnectionHandler to perform the necessary operations.
    """

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        """
        Initializes the LogsRepository with a database connection.

        :param db_connection: An instance of DBConnectionHandler to manage database interactions.
        """
        self.__collection_name = "logs"
        self.__db_connection = db_connection

    def save(self, log: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(log)
