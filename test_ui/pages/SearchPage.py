from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import allure

class SearchPage:
    def __init__(self, driver):
        """
        Конструктор класса SearchPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._wait = WebDriverWait(driver, 30)

    @allure.step("Открытие сайта Кинопоиск")
    def open(self):
        """
        Открывает главную страницу сайта Кинопоиск
        """
        self._driver.get("https://www.kinopoisk.ru/")

    @allure.step ("Поиск фильма")
    def input_movie(self):
        """
        Ввод названия фильма в поисковую строку
        :param: name - название фильма
        """
        movie_input = self._driver.find_element(By.XPATH, '//input[@name="kp_query"]')
        movie_input.send_keys("Роднина", Keys.RETURN)

    @allure.step ("Выбор нужного фильма")
    def click_movie(self):
        """
        Нажимает на название фильма на странице с результатами
        """
        self._driver.find_element(By.XPATH, '//a[text()="Роднина"]').click()

    @allure.step("Возврат на главную страницу")
    def go_main_page(self):
        """
        Осуществляет переход на главную страницу сайта
        :param: img - иконка с названием Кинопоиск
        """
        self._driver.find_element(By.XPATH, '//img[@alt="Кинопоиск"]').click()




