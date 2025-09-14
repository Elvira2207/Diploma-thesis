from pages.CinemaPage import CinemaPage
import allure

@allure.title ("Тестирование Онлайн-кинотеатра")
@allure.feature ("Онлайн-кинотеатр")
@allure.description ("Тест проверяет работу кнопок, иконок на странице Онлайн-кинотеатра")
@allure.severity (allure.severity_level.CRITICAL)
def test_cinema(browser):
    """
    Тест проверяет переходы при нажатии на кнопки, иконки, логотипы
    :param browser: Webdriver - объект драйвера, переданный фикстурой
    """
    cinema_page = CinemaPage(browser)
    with allure.step("Переход в Онлайн-кинотеатр"):
        cinema_page.online_cinema()

    with allure.step("Переход на страницу Каналы"):
        cinema_page.icon_channels()

    with allure.step("Выбор каналов"):
        cinema_page.watch_childrens()
