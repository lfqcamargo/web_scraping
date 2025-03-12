from ..settings.connection_handler import DBConnectionHandler
from .logs_repository import LogsRepository


db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


def test_insert_log() -> None:
    """
    Test Repository
    """
    log_repository = LogsRepository(conn)
    log = {"log": "Teste"}
    log_repository.save(log)
