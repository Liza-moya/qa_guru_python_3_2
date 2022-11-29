import random
from selene import browser, config
import pytest


@pytest.fixture(scope="session")
def open_browser():
    b = browser.open_url('https://google.com/ncr')
    print("Браузер открыт")
    yield b
    #
    # print(f"Случайное число: {random.randint(0, 100)}")
    # yield b
    # b = ""
    print("Браузер закрыт!")

   br = browser(Config(
        driver = Chrome(),
        base_url='https://google.com',
       timeout=2))