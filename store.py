from selenium.webdriver.common.by import By

from driver import Driver
from config import config


class Store:
    _about_xpath = config["locators"]["about_link"]
    _navbar_xpath = config["locators"]["navbar"]
    _slider_xpath = config["locators"]["slider"]

    @staticmethod
    def verify_page():
        Driver().get_driver().find_element(By.XPATH, Store._navbar_xpath)
        Driver().get_driver().find_element(By.XPATH, Store._slider_xpath)

    @staticmethod
    def open_about():
        about = Driver().get_driver().find_element(By.XPATH, Store._about_xpath)
        about.click()
