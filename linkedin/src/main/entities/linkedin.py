import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


class Linkedin:
    def __init__(self) -> None:
        self.__driver = webdriver.Chrome()
        self.__web_site = "https://br.linkedin.com/"
        self.__email = os.getenv("EMAIL")
        self.__password = os.getenv("PASSWORD")

    def execute(self) -> None:
        self.__driver.maximize_window()
        self.__access_website()
        self.__login()
        self.__access_jobs()
        self.__find_jobs()

    def __access_website(self) -> None:
        try:
            self.__driver.get(self.__web_site)
            time.sleep(2)
            self.__driver.find_element(By.LINK_TEXT, "Entrar").click()
            time.sleep(2)
        except Exception as e:
            raise e

    def __login(self) -> None:
        try:
            form_login = self.__driver.find_element(By.CLASS_NAME, "login__form")
            form_login.find_element(By.ID, "username").send_keys(self.__email)
            form_login.find_element(By.ID, "password").send_keys(self.__password)
            form_login.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            # Wait to confirmation 10 minutes
            try:
                WebDriverWait(self.__driver, 600).until(
                    EC.presence_of_element_located((By.ID, "global-nav-search"))
                )
            except Exception as e:
                raise e
        except Exception as e:
            raise e

    def __access_jobs(self) -> None:
        try:
            self.__driver.find_element(By.CSS_SELECTOR, "a[href*='jobs']").click()
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "jobs-home-vertical-list__entity-list")
                )
            )
            div_a = self.__driver.find_element(
                By.CLASS_NAME, "discovery-templates-vertical-list__footer"
            )
            div_a.find_element(By.TAG_NAME, "a").click()

            # Wait load
            WebDriverWait(self.__driver, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "scaffold-layout__list-detail-container")
                )
            )

        except Exception as e:
            raise e

    def __find_jobs(self) -> None:
        while True:
            try:
                self.__jobs_simplified()
            except Exception as e:
                print(e)
                continue

    def __jobs_simplified(self) -> None:
        self.__driver.find_element(
            By.XPATH, "//a[text()='Candidatura simplificada']"
        ).click()

        list_jobs = self.__get_list_jobs()

        for item in list_jobs:
            div_element = item.find_element(By.TAG_NAME, "div")
            div_element.find_element(By.TAG_NAME, "div").click()

    def __get_list_jobs(self) -> list[WebElement]:
        return self.__driver.find_elements(
            By.CLASS_NAME,
            "ember-view.yRtVjzsdJLVItpTIUgbyCFReVmBEnTirciqI.occludable-update.p0.relative.scaffold-layout__list-item",
        )
