from abc import ABC, abstractmethod


class LogsRepositoryInterface(ABC):

    @abstractmethod
    def save(self, log: dict):
        raise NotImplementedError("Subclasses must implement the save method")
