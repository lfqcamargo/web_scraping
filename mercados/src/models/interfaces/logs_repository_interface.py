from abc import ABC, abstractmethod
from src.main.entities.log import Log


class LogsRepositoryInterface(ABC):
    """
    Interface for the Logs Repository.

    This abstract class defines the contract for any implementation
    of a logs repository, ensuring consistency in logging operations.
    """

    @abstractmethod
    def save(self, log: Log) -> None:
        """
        Saves a log entry into the database.

        This method must be implemented by any concrete repository class
        to persist log data.

        :param log: A dictionary containing log details.
        """
        raise NotImplementedError("Subclasses must implement the save method")
