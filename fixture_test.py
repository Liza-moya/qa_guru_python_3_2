import pytest
import random
import math


@pytest.fixture()
def create_user(open_browser):
    return "username", "password"


def test_body(open_browser, create_user):
    assert open_browser == "browser"
    assert create_user == 25
    # Перейти на страницу логина
    # Ввести логин и пароль
    # Нажать ОК
    # Убедиться что мы перешли на страницу профиля


def test_body2(open_browser, create_user):
    pass


def test_body3(open_browser, create_user):
    pass