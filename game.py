from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import config
from driver import Driver


class Game:
    _name_xpath = '//*[@id="appHubAppName"]'
    _release_date_xpath = '//*[@class="date"]'
    _price_xpath = '//*[@class="game_area_purchase_game_wrapper"]//*[@class="game_purchase_price price"]'

    @staticmethod
    def wait_find(xpath):
        return WebDriverWait(Driver().get_driver(), config["waiting_time"]).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )
    @staticmethod
    def get_attr():
        name = Game.wait_find(Game._name_xpath)
        name_text = Driver().get_driver().execute_script("return arguments[0].innerText;", name)
        release_date = Driver().get_driver().find_element(By.XPATH, Game._release_date_xpath)
        release_date_text = Driver().get_driver().execute_script("return arguments[0].innerText;", release_date)
        price = Driver().get_driver().find_element(By.XPATH, Game._price_xpath)
        price_text = Driver().get_driver().execute_script("return arguments[0].innerText;", price)

        return name_text, release_date_text, price_text
