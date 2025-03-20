import pytest

from config import config
from driver import Driver


@pytest.fixture(autouse=True)
def browser() -> Driver:
    driver = Driver().get_driver()
    driver.get(config["base_url"])
    yield driver
    Driver().quit_driver()
