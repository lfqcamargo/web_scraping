from ...interfaces.products_repository_interface import ProductsRepositoryInterface
from ..settings.connection_handler import DBConnectionHandler


class ProductsRepository(ProductsRepositoryInterface):
    """
    Repository for handling product-related database operations.

    This class provides methods to interact with the 'products' collection
    in the database, ensuring that product data is properly managed.
    """

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        """
        Initializes the ProductsRepository with a database connection.

        :param db_connection: An instance of DBConnectionHandler to manage database interactions.
        """
        self.__collection_name = "products"
        self.__db_connection = db_connection

    def save(self, product: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(product)
