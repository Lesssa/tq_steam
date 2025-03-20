from selenium import webdriver


class Driver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--incognito")
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome(options=options)
            cls._instance.driver.implicitly_wait(5)
        return cls._instance

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self._instance = None
