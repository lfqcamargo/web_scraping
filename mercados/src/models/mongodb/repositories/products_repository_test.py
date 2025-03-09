from datetime import date
from ..settings.connection_handler import DBConnectionHandler
from .products_repository import ProductsRepository


db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


def test_insert_product() -> None:
    """
    Test Repository
    """
    product_repository = ProductsRepository(conn)
    product = {
        "date": date.today().strftime("%d-%m-%Y"),
        "product": "Coca-Cola",
        "category": "Drink",
        "price": 15.68,
    }
    product_repository.save(product)
