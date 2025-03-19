import pytest

from driver import Driver


@pytest.fixture(scope="session")
def browser() -> Driver:
    driver = Driver()
    driver.set_window_size(1920, 1080)
    driver.get("https://store.steampowered.com/")

    yield driver

    driver.quit()
    Driver._instance = None
