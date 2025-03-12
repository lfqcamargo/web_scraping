from pymongo import MongoClient
from pymongo.database import Database


class DBConnectionHandler:
    """
    Handles the connection to a MongoDB database.

    This class manages the connection to a MongoDB instance, providing methods
    to establish a connection and retrieve the database object.

    Attributes:
        __connection_string (str): The MongoDB connection URI.
        __database_name (str): The name of the target database.
        __client (MongoClient | None): The MongoDB client instance.
        __db_connection (Database | None): The active database connection.
    """

    def __init__(self) -> None:
        """
        Initializes the class for handling MongoDB database connections.
        Defines the connection string, database name, and initializes
        variables for the client and database connection.
        """
        # self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
        #     "admin", "admin", "localhost", "27017"
        # )
        self.__connection_string = "mongodb://localhost:27017/"
        self.__database_name = "scraping_markets"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        """
        Establishes the connection to MongoDB using the provided connection string.
        The connection is made to the database specified in self._database_name.
        """
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self) -> None | Database:
        """
        Returns the active MongoDB database connection.

        :return: The database connection object.
        """
        return self.__db_connection


db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
db_connection = db_connection_handler.get_db_connection()
