import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser

    browser.implicitly_wait(20)
    browser.quit()
