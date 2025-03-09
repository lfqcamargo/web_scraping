from src.models.mongodb.settings.connection_handler import db_connection
from src.models.mongodb.repositories.products_repository import ProductsRepository
from src.main.entities.central import Central

db_connection_handler = db_connection

central_composer = ProductsRepository(db_connection)
central = Central(central_composer)
