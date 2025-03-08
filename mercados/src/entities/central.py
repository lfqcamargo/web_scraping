import time
import selenium
import selenium.common
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from src.entities.interfaces.market import Market


class Central(Market):
    """
    Represents the Central market. Implements the methods to
    interact with the Central market's website.

    This subclass provides the specific logic for inserting a CEP and extracting products
    from the Central market's website using Selenium WebDriver.

    Attributes:
        driver (webdriver.Chrome): Selenium WebDriver instance used to interact with the website.
    """

    def __init__(self) -> None:
        self.__driver = webdriver.Chrome()

    def execute(self) -> None:
        self.insert_cep()
        self.browse_categories()

    def insert_cep(self) -> None:
        self.__driver.get("https://www.supercentralonline.com.br/")
        self.__driver.maximize_window()
        cont = 0

        try:
            cep = WebDriverWait(self.__driver, 15).until(
                EC.presence_of_element_located((By.ID, "cep"))
            )

        except selenium.common.exceptions.TimeoutException:
            button_cep = self.__driver.find_element(
                By.CLASS_NAME, "btn.btn-warning.ng-star-inserted"
            )
            button_cep.click()
        finally:
            time.sleep(2)
            cep = self.__driver.find_element(By.ID, "cep")

        cep.send_keys("18654-632")
        time.sleep(4)

        cont = 0

        while True:
            try:
                button_delivery = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "alterar-loja--opcao.ng-star-inserted")
                    )
                )
                button_delivery.click()

                if button_delivery is not None:
                    button_select_cep = WebDriverWait(self.__driver, 10).until(
                        EC.presence_of_element_located(
                            (
                                By.CLASS_NAME,
                                "btn.address--button__selecionar.btn-block.btn-default",
                            )
                        )
                    )
                    button_select_cep.click()
            except selenium.common.exceptions.TimeoutException as e:
                print(e)
            time.sleep(4)
            cont += 1
            if button_select_cep is not None or cont > 3:
                break

    def browse_categories(self):
        list_categories = self.__driver.find_elements(By.CLASS_NAME, "featured")

        for category in list_categories:
            category.click()
            time.sleep(2)
            list_item = self.__driver.find_elements(
                By.CLASS_NAME,
                "center-block.image-category.ng-lazyloaded",
            )

            for index in range(len(list_item)):
                try:
                    list_item = self.__driver.find_elements(
                        By.CLASS_NAME, "center-block.image-category.ng-lazyloaded"
                    )
                    item = list_item[index]

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

                    time.sleep(2)
                    self.browse_products()
                    self.__driver.back()
                    time.sleep(2)
                except Exception as e:
                    pass

    def browse_products(self):
        try:
            list_products = self.__driver.find_elements(
                By.CLASS_NAME,
                "col-xs-6.col-sm-3.col-md-3.col-lg-3.product.ng-star-inserted",
            )

            for index in range(len(list_products)):
                list_item = self.__driver.find_elements(
                    By.CLASS_NAME,
                    "col-xs-6.col-sm-3.col-md-3.col-lg-3.product.ng-star-inserted",
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
                time.sleep(2)
                self.__driver.back()
                time.sleep(2)
        except Exception as e:
            print(e)
            pass
