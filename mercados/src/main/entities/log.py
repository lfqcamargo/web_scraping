from datetime import datetime
from typing import Optional


class Log:
    def __init__(self, market: str) -> None:
        self.__start_date: datetime = datetime.now()
        self.end_date: Optional[datetime] = None
        self.market: str = market
        self.total_category: Optional[int] = None
        self.total_item_per_category: list[dict] = None
        self.logs_error: list[dict] = []

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    def to_dict(self) -> dict:
        log = {
            "start_date": self.__start_date.strftime("%d/%m/%Y %H:%M"),
            "end_date": self.end_date.strftime("%d/%m/%Y %H:%M"),
            "market": self.market,
            "total_category": self.total_category,
            "total_item_per_category": self.total_item_per_category,
            "logs_error": self.logs_error,
        }

        return log
