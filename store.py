from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from driver import Driver


class Store:
    _about_xpath = '//a[@class = "menuitem " and contains(@href, "about") and contains(@href, "global-header")]'
    _navbar_xpath = '//*[@id="store_nav_area"]'
    _recommended_xpath = '//*[@id="home_featured_and_recommended"]'
    _noteworthy_xpath = '//*[@id="noteworthy_tab"]'
    #_noteworthy_popup_xpath = '//*[@id="noteworthy_flyout" and contains(@style, "display: block")]'
    _topselling_xpath = '//a[@class="popup_menu_item" and contains(@href, "topselling")]'
    @staticmethod
    def verify_page():
        Driver().get_driver().find_element(By.XPATH, Store._navbar_xpath)
        Driver().get_driver().find_element(By.XPATH, Store._recommended_xpath)

    @staticmethod
    def open_about():
        about = Driver().get_driver().find_element(By.XPATH, Store._about_xpath)
        about.click()

    @staticmethod
    def expand_noteworthy():
        noteworthy = Driver().get_driver().find_element(By.XPATH, Store._noteworthy_xpath)
        ActionChains(Driver().get_driver()).move_to_element(noteworthy).perform()
        wait = WebDriverWait(Driver().get_driver(), 5)
        topselling = wait.until(ec.visibility_of_element_located((By.XPATH, Store._topselling_xpath)))
        topselling.click()

