import pytest

from config import config
from driver import Driver


@pytest.fixture(autouse=True)
def browser() -> Driver:
    driver = Driver().get_driver()
    driver.set_window_size(1920, 1080)
    driver.get(config["base_url"])

    yield driver
    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}
