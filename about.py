import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from driver import Driver


class About:
    _stats_xpath = '//*[@class = \'online_stat\']'
    _greeting_xpath = '//*[@id = \'about_greeting\']'

    @staticmethod
    def wait_for_loader_off():
        WebDriverWait(Driver().get_driver(), 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, About._stats_xpath)))

    @staticmethod
    def verify_page():
        About.wait_for_loader_off()
        Driver().get_driver().find_element(By.XPATH, About._greeting_xpath)

    @staticmethod
    def get_stats():
        num_stats = []
        online_stats = Driver().get_driver().find_elements(By.XPATH, About._stats_xpath)
        for st in online_stats:
            stats = Driver().get_driver().execute_script("return arguments[0].innerText;", st)
            stats = re.sub(r'\D', '', stats)
            num_stats.append(int(stats))
        return num_stats
