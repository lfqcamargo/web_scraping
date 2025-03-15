from datetime import date, datetime
from typing import List
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from src.models.interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.models.interfaces.logs_repository_interface import LogsRepositoryInterface
from src.main.entities.log import Log
from src.main.entities.log_error import LogError


class Central:
    """
    Represents the Central market. Implements the methods to
    interact with the Central market's website.

    This subclass provides the specific logic for inserting a CEP and extracting products
    from the Central market's website using Selenium WebDriver.

    Attributes:
        driver (webdriver.Chrome): Selenium WebDriver instance used to interact with the website.
    """

    def __init__(
        self,
        products_repository: ProductsRepositoryInterface,
        logs_repository: LogsRepositoryInterface,
    ) -> None:
        self.__driver = webdriver.Chrome()
        self.__products_repository = products_repository
        self.__logs_repository = logs_repository
        self.__log = Log("Central")

    def execute(self) -> None:
        try:
            self.insert_cep()
            time.sleep(2)
            list_categories = self.get_categories()
            self.__log.total_category = len(list_categories)

            for category in list_categories:
                try:
                    list_sub_categories = self.get_sub_categories(category)
                    total_item_per_category = self.browse_sub_categories_and_products(
                        list_sub_categories
                    )
                    self.__log.total_item_per_category = {}

                except Exception:
                    date_time = datetime.now()
                    message = "Unable to scroll through category list"
                    log_error = LogError(date_time, message, Exception)
                    self.__log.logs_error.append(log_error.to_dict())

        finally:
            self.__logs_repository.save(self.__log.to_dict())

        return None

    def insert_cep(self) -> None:
        self.__driver.get("https://www.supercentralonline.com.br/")
        self.__driver.maximize_window()

        try:
            cep = WebDriverWait(self.__driver, 15).until(
                EC.presence_of_element_located((By.ID, "cep"))
            )
        except Exception:
            try:
                self.__driver.find_element(
                    By.CLASS_NAME, "btn.btn-warning.ng-star-inserted"
                ).click()
                cep = WebDriverWait(self.__driver, 15).until(
                    EC.presence_of_element_located((By.ID, "cep"))
                )
            except Exception:
                date_time = datetime.now()
                message = "Unable to enter zip code"
                log_error = LogError(date_time, message, Exception)
                self.__log.logs_error.append(log_error.to_dict())
                return

        cep.send_keys("18654-632")

        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "alterar-loja--opcao.ng-star-inserted")
                )
            ).click()

            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        "btn.address--button__selecionar.btn-block.btn-default",
                    )
                )
            ).click()

        except Exception as e:
            date_time = datetime.now()
            message = "Unable to select location"
            log_error = LogError(date_time, message, e)
            self.__log.logs_error.append(log_error.to_dict())
            raise e

        return None

    def get_categories(self) -> List[WebElement]:
        try:
            list_categories = self.__driver.find_elements(By.CLASS_NAME, "featured")
        except Exception as e:
            date_time = datetime.now()
            message = "Unable to scroll through category list"
            log_error = LogError(date_time, message, e)
            self.__log.logs_error.append(log_error.to_dict())
            return e

        return list_categories

    def get_sub_categories(self, category: WebElement) -> List[WebElement]:
        category.click()
        list_sub_categories = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_all_elements_located(
                (
                    By.CLASS_NAME,
                    "center-block.image-category.ng-lazyloaded",
                )
            )
        )
        return list_sub_categories

    def browse_sub_categories_and_products(
        self, list_sub_categories: List[WebElement]
    ) -> int:
        try:
            total_item_per_category = 0
            for index in range(len(list_sub_categories)):
                try:
                    list_sub_categories = self.__driver.find_elements(
                        By.CLASS_NAME, "center-block.image-category.ng-lazyloaded"
                    )
                    item = list_sub_categories[index]

                    WebDriverWait(self.__driver, 10).until(
                        EC.element_to_be_clickable(item)
                    )

                    self.__driver.execute_script(
                        "arguments[0].scrollIntoView(true);", item
                    )
                    body = self.__driver.find_element(By.TAG_NAME, "body")
                    actions = ActionChains(self.__driver)
                    actions.move_to_element(body).perform()
                    actions.move_to_element(item).click().perform()

                    self.browse_products()
                    self.__driver.back()
                    time.sleep(2)
                    total_item_per_category += 1
                except Exception:
                    continue
        except Exception:
            date_time = datetime.now()
            message = "Unable to scroll through category list"
            log_error = LogError(date_time, message, Exception)
            self.__log.logs_error.append(log_error.to_dict())
            return None
        return total_item_per_category

    def browse_products(self) -> None:
        try:
            list_products = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (
                        By.CLASS_NAME,
                        "col-xs-6.col-sm-3.col-md-3.col-lg-3.product.ng-star-inserted",
                    )
                )
            )

            for index in range(len(list_products)):
                try:
                    list_item = self.__driver.find_elements(
                        By.CLASS_NAME,
                        "thumbnail.produto-disponivel.ng-star-inserted",
                    )
                    product = list_item[index]

                    WebDriverWait(self.__driver, 10).until(
                        EC.element_to_be_clickable(product)
                    )

                    self.__driver.execute_script(
                        "arguments[0].scrollIntoView(true);", product
                    )

                    actions = ActionChains(self.__driver)
                    body = self.__driver.find_element(By.TAG_NAME, "body")
                    actions.move_to_element(body).perform()
                    actions.move_to_element(product).click().perform()
                    time.sleep(3)
                    self.save_product()
                    self.__driver.back()
                    time.sleep(2)
                except Exception:
                    continue
        except Exception:
            date_time = datetime.now()
            message = "Unable to scroll through products list"
            log_error = LogError(date_time, message, Exception)
            self.__log.logs_error.append(log_error.to_dict())
            return None
        return None

    def save_product(self) -> None:
        try:
            nav_category_product = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "vip-tabs-bar.ng-star-inserted")
                )
            )

            category_product = nav_category_product.find_element(
                By.CLASS_NAME, "ng-star-inserted"
            )
            title_product = self.__driver.find_element(By.TAG_NAME, "h3")
            price_product = self.__driver.find_element(
                By.CLASS_NAME, "info-price.ng-star-inserted"
            )

            product = {
                "date": date.today().strftime("%d-%m-%Y"),
                "product": title_product.text,
                "category": category_product.text,
                "price": price_product.text,
            }
            print(product)
            try:
                self.__products_repository.save(product)
            except Exception:
                date_time = datetime.now()
                message = f"Error trying to save product {product}"
                log_error = LogError(date_time, message, Exception)
                self.__log.logs_error.append(log_error.to_dict())
                return None

        except Exception:
            return None
        return None
