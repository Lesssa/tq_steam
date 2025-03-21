from selenium import webdriver

from config import config


class Driver:
    _instance = None

    def __new__(cls):
        browser_name = config["browser"].lower()
        options = None
        if cls._instance is None:
            if browser_name == "chrome":
                options = webdriver.ChromeOptions()
            else:
                raise Exception(f"Browser {browser_name} is not supported")
            for arg in config["browser_options"]:
                options.add_argument(arg)
            cls._instance = super().__new__(cls)
            cls._instance.driver = cls._create_driver(browser_name, options)
        return cls._instance

    @staticmethod
    def _create_driver(browser_name, options):
        if browser_name == "chrome":
            return webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self._instance = None
