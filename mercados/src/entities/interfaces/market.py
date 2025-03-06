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
