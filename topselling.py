import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import config
from driver import Driver


class Topselling:
    _more_button_xpath = '//button[contains(@class, "DialogButton")]'
    _topselling_sidebar_xpath = '//a[@href = "/charts/topselling/LV"]'
    _charts_xpath = '//a[contains(@href, "/charts/topsellers")]'
    _price_range_xpath = '//*[@data-collapse-name="price"]'
    _linux_checkbox_xpath = '//*[@data-value="linux" and contains(@class, "tab_filter_control_include")]'
    _gamers_amount_menu_xpath = '//*[contains(text(), "Количество игроков")]'
    _lan_checkbox_xpath = '//*[@data-loc="Кооператив (локальная сеть)" and @class="tab_filter_control_row "]'
    _action_label_xpath = '//*[@data-loc="Экшен" and @class="tab_filter_control_row "]'
    _filtered_results_info_xpath = '//*[@id="search_results_filtered_warning_persistent"]'
    _filtered_games_xpath = '//*[contains(@class, "search_result_row")]'
    _filtered_xpath = '//*[@id="search_result_container"]'
    _first_game_xpath = '//*[@id="search_resultsRows"]/child::*[1]'
    _first_game_name_xpath = '//*[@id="search_resultsRows"]/child::*[1]//*[@class="title"]'
    _first_game_release_xpath = '//*[@id="search_resultsRows"]/child::*[1]//*[@class="col search_released responsive_secondrow"]'
    _first_game_price_xpath = '//*[@id="search_resultsRows"]/child::*[1]//*[contains(@class, "discount_final_price")]'
    _tags_list_xpath = '//*[@data-collapse-name="tags"]'
    _gamers_list_xpath = '//*[@data-collapse-name="category3"]'
    _os_list_xpath = '//*[@data-collapse-name="os"]'


    @staticmethod
    def find_move_element(xpath, click=False, expand=False):
        if click and expand:
            raise ValueError("Нельзя использовать одновременно флаги 'click' и 'expand'. Выберите только один.")

        element = Topselling.wait_find(xpath)
        ActionChains(Driver().get_driver()).move_to_element(element).perform()
        if expand:
            Topselling.check_if_collapsed(element)
        if click:
            element.click()

    @staticmethod
    def verify_page():
        Topselling.wait_find(Topselling._topselling_sidebar_xpath)
        Driver().get_driver().find_elements(By.XPATH, Topselling._charts_xpath)

    @staticmethod
    def wait_find(xpath):
        return WebDriverWait(Driver().get_driver(), config["waiting_time"]).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )

    @staticmethod
    def open_more_topselling():
        Topselling.find_move_element(Topselling._more_button_xpath, click=True)
        Topselling.wait_find(Topselling._price_range_xpath)

    @staticmethod
    def check_if_collapsed(element):
        classes = element.get_attribute("class")
        if "collapsed" in classes:
            element.click()

    @staticmethod
    def filter_topselling():
        Topselling.find_move_element(Topselling._os_list_xpath, expand=True)
        Topselling.find_move_element(Topselling._linux_checkbox_xpath, click=True)
        Topselling.find_move_element(Topselling._gamers_list_xpath, expand=True)
        time.sleep(1)
        lan_checkbox = Topselling.wait_find(Topselling._lan_checkbox_xpath)
        lan_checkbox.click()
        Topselling.find_move_element(Topselling._tags_list_xpath, expand=True)
        Topselling.find_move_element(Topselling._action_label_xpath, click=True)


    @staticmethod
    def get_results():
        result_container = Topselling.wait_find(Topselling._filtered_xpath)
        WebDriverWait(Driver().get_driver(), config["waiting_time"]).until(
            lambda driver: result_container.get_attribute("style") is not None
        )
        WebDriverWait(Driver().get_driver(), config["waiting_time"]).until(
            ec.presence_of_element_located((By.XPATH, Topselling._filtered_xpath))
        )

        results = Topselling.wait_find(Topselling._filtered_results_info_xpath)
        results_text = Driver().get_driver().execute_script("return arguments[0].innerText;", results)

        found_games_real = len(Driver().get_driver().find_elements(By.XPATH, Topselling._filtered_games_xpath))
        found_games_info = int(re.search(r"\d+", results_text).group())

        return found_games_info, found_games_real

    @staticmethod
    def get_first_game_attr():
        name = Topselling.wait_find(Topselling._first_game_name_xpath)
        name_text = Driver().get_driver().execute_script("return arguments[0].innerText;", name)
        release_date = Driver().get_driver().find_element(By.XPATH, Topselling._first_game_release_xpath)
        release_date_text = Driver().get_driver().execute_script("return arguments[0].innerText;", release_date)
        price = Driver().get_driver().find_element(By.XPATH, Topselling._first_game_price_xpath)
        price_text = Driver().get_driver().execute_script("return arguments[0].innerText;", price)
        return name_text, release_date_text, price_text

    @staticmethod
    def open_first_game():
        first_game = Topselling.wait_find(Topselling._first_game_xpath)
        first_game.click()

