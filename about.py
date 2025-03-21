import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import config
from driver import Driver


class About:
    _stats_xpath = '//*[@class = \'online_stat\']'
    _greeting_xpath = '//*[@id = \'about_greeting\']'
    _store_xpath = '//a[@class = "menuitem supernav" and @data-tooltip-content=".submenu_Store" and contains(@href, "global-header")]'

    @staticmethod
    def wait_find(xpath):
        return WebDriverWait(Driver().get_driver(), config["waiting_time"]).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )


    @staticmethod
    def verify_page():
        About.wait_find(About._stats_xpath)
        About.wait_find(About._greeting_xpath)

    @staticmethod
    def get_stats():
        num_stats = []
        online_stats = Driver().get_driver().find_elements(By.XPATH, About._stats_xpath)
        for st in online_stats:
            stats = Driver().get_driver().execute_script("return arguments[0].innerText;", st)
            stats = re.sub(r'\D', '', stats)
            num_stats.append(int(stats))
        return num_stats

    @staticmethod
    def go_to_main():
        about = About.wait_find(About._store_xpath)
        about.click()
