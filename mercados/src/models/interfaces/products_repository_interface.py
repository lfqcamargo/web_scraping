from abc import ABC, abstractmethod


class ProductsRepositoryInterface(ABC):
    """
    Interface for the Products Repository.

    This abstract class defines the contract for any implementation
    of a products repository, ensuring consistency in data operations.
    """

    @abstractmethod
    def save(self, product: dict) -> None:
        """
        Saves a product into the database.

        This method must be implemented by any concrete repository class
        to persist product data.

        :param product: A dictionary containing product details.
        """
        raise NotImplementedError("Subclasses must implement the save method")
