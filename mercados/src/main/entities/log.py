from datetime import datetime


class Log:
    """
    A Log class represents a log entry, containing details such as the timestamp,
    message, and exception information.

    This class is used to create log entries that can be saved to a database or
    displayed for debugging purposes.
    """

    def __init__(self, date_time: datetime, message: str, exception: Exception) -> None:
        """
        Initializes a new Log instance.

        :param datetime: The timestamp of when the log entry was created.
        :param message: A string message describing the log entry.
        :param exception: An optional exception associated with the log entry.
        """
        self.date_time = date_time
        self.message = message
        self.exception = exception

    def to_dict(self) -> dict:
        """
        Converts the Log instance into a dictionary format suitable for logging.

        This method formats the log's timestamp as a string and prepares the message
        and exception for storage in a database or display.

        :return: A dictionary representing the log, with datetime, message, and exception fields.
        """
        log = {
            "datetime": self.date_time.strftime("%d/%m/%Y %H:%M"),
            "message": self.message,
            "exception": str(self.exception.args),
        }

        return log
