from selenium.webdriver.common.by import By

from driver import Driver


class Game:
    _name_xpath = '//*[@id="appHubAppName"]'
    _release_date_xpath = '//*[@class="date"]'
    _price_xpath = '//*[@class="game_area_purchase_game_wrapper"]//*[@class="game_purchase_price price"]'

    @staticmethod
    def get_attr():
        name = Driver().get_driver().find_element(By.XPATH, Game._name_xpath)
        name_text = Driver().get_driver().execute_script("return arguments[0].innerText;", name)
        release_date = Driver().get_driver().find_element(By.XPATH, Game._release_date_xpath)
        release_date_text = Driver().get_driver().execute_script("return arguments[0].innerText;", release_date)
        price = Driver().get_driver().find_element(By.XPATH, Game._price_xpath)
        price_text = Driver().get_driver().execute_script("return arguments[0].innerText;", price)

        return name_text, release_date_text, price_text
