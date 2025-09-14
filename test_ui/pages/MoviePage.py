from selenium.webdriver.common.by import By
import allure

class MoviePage:
    def __init__(self, driver):
        """
        Конструктор класса MoviePage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get("https://www.kinopoisk.ru/")
        """
        Открывает главную страницу сайта Кинопоиск
        """

    @allure.step ("Информация о главном актере")
    def click_actor(self):
        """
        Выбирает и нажимает на актера в списке
        """
        self._driver.find_element(By.XPATH, '//a[text()="Владислава Самохина"]').click()

    @allure.step ("Возврат на главную страницу")
    def go_main_page(self):
        """
        Осуществляет переход на главную страницу сайта
        :param: img - иконка с названием Кинопоиск
        """
        self._driver.find_element(By.XPATH, '//img[@alt="Кинопоиск"]').click()