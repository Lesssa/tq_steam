from selenium.webdriver.common.by import By

from driver import Driver


class Store:
    _about_xpath = '//a[@class = \'menuitem \' and contains(@href, \'about\') and contains(@href, \'global-header\')]'
    _navbar_xpath = '//*[@id=\'store_nav_area\']'
    _slider_xpath = '//*[@id=\'home_hero_ctn\']'

    @staticmethod
    def verify_page():
        Driver().find_element(By.XPATH, Store._navbar_xpath)
        Driver().find_element(By.XPATH, Store._slider_xpath)

    @staticmethod
    def open_about():
        about = Driver().find_element(By.XPATH, Store._about_xpath)
        about.click()
