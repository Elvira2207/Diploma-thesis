from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

class CinemaPage:
    def __init__(self, driver):
        """
        Конструктор класса CinemaPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    @allure.step ("Открытие сайта Кинопоиск")
    def open(self):
        self._driver.get("https://www.kinopoisk.ru/")
        """
        Открывает главную страницу сайта Кинопоиск
        """

    @allure.step ("Переход в Онлайн-кинотеатр")
    def online_cinema(self):
        """
        Открывает страницу онлайн-кинотеатра, путем нажатия на на иконку в шапке сайта
        """
        self._driver.find_element(By.XPATH, '//a[@data-tid="acc26a70"]').click()

    @allure.step ("Переход на страницу Каналы")
    def icon_channels(self):
        """
        Нажимает на иконку "Каналы" и открывает страницу всех каналов для выбора просмотра
        """
        self._driver.find_element(By.ID, 'channels').click()

    @allure.step ("Выбор каналов")
    def watch_childrens(self):
        """
        Нажимает на выбранную иконку по тематике
        """
        self._driver.find_element(By.XPATH, '//button[text()="Детские"]').click()