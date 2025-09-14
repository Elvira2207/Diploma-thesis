from selenium.webdriver.common.by import By
import allure

class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
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

    @allure.step ("Возврат на главную страницу")
    def return_main(self):
        """
        Переходит на главную страницу, путем нажатия на логотип Кинопоиск
        """
        self._driver.find_element(By.XPATH, '//*[@data-tid="LogoKP"]').click()

    @allure.step ("Переход на страницу Билеты в кино")
    def movie_tickets(self):
        """
        Нажимает на кнопку 'Билеты в кино'
        """
        self._driver.find_element(By.XPATH, '//span[text()="Билеты в кино"]').click()
        """
        Открывается страница выбора билетов
        """