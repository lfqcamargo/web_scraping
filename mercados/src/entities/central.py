import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from mercados.src.entities.interfaces.market import Market


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

    def insert_cep(self) -> None:
        self.__driver.get("https://www.supercentralonline.com.br/")
        self.__driver.maximize_window()
        cont = 0

        while True:
            cep = WebDriverWait(self.__driver, 15).until(
                EC.presence_of_element_located((By.ID, "cep"))
            )

            if cep is None:
                button_cep = self.__driver.find_element(
                    By.CLASS_NAME, "btn.btn-warning.ng-star-inserted"
                )
                button_cep.click()

                cep = self.__driver.find_element(By.ID, "cep")

            cont += 1
            time.sleep(1)

            if cep is not None or cont >= 10:
                break

        cep.send_keys("18654-632")
        time.sleep(4)

        cont = 0

        while True:
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

            time.sleep(4)
            cont += 1
            if button_select_cep is not None or cont > 3:
                break
