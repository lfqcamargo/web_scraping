from src.models.mongodb.settings.connection_handler import db_connection
from src.models.mongodb.repositories.products_repository import ProductsRepository
from src.models.mongodb.repositories.logs_repository import LogsRepository
from src.main.entities.central import Central


products_repository = ProductsRepository(db_connection)
logs_repository = LogsRepository(db_connection)

central = Central(products_repository, logs_repository)
