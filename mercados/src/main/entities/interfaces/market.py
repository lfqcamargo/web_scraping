from abc import ABC, abstractmethod


class Market(ABC):
    """
    Abstract base class for market entities. This class defines the common interface
    for all markets. Each subclass must implement the methods for interacting with
    a specific market's website.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the process of inserting a CEP into the Central market's website.
        """

    @abstractmethod
    def insert_cep(self) -> None:
        """
        Abstract method to insert a CEP (postal code) into the market's website.

        This method should be implemented by concrete market classes to provide the specific
        logic for inserting a CEP.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
        """
        raise NotImplementedError("Subclasses must implement the insert_cep method")

    @abstractmethod
    def browse_categories(self) -> None:
        """
        Abstract method to browse and extract product categories from the market's website.

        This method should be implemented by concrete market classes to provide the specific
        logic for browsing and retrieving the categories of products available on the market's
        website.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
        """
        raise NotImplementedError(
            "Subclasses must implement the browse_categories method"
        )

    @abstractmethod
    def browse_products(self) -> None:
        """
        Abstract method to browse and extract product details from the market's website.

        This method should be implemented by concrete market classes to provide the specific
        logic for browsing and retrieving product information from the market's website.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
        """
        raise NotImplementedError(
            "Subclasses must implement the browse_products method"
        )

    @abstractmethod
    def save_product(self) -> None:
        """
        Abstract method to save product data extracted from the market's website.

        This method should be implemented by concrete market classes to handle the storage
        of product information, whether in a database, a file, or another storage system.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
        """
        raise NotImplementedError("Subclasses must implement the save_product method")
