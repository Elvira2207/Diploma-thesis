from pages.MainPage import MainPage
import allure

@allure.title ("Тестирование главной страницы")
@allure.feature ("Кинопоиск")
@allure.description ("Тест проверяет работу кнопок, иконок на главной странице")
@allure.severity (allure.severity_level.CRITICAL)
def test_main_page(browser):
    """
    Тест проверяет переходы при нажатии на кнопки, иконки, логотипы
    :param browser: Webdriver - объект драйвера, переданный фикстурой
    """
    main_page = MainPage(browser)
    with allure.step("Переход в Онлайн-кинотеатр"):
        main_page.online_cinema()

    with allure.step("Возврат на главную страницу"):
        main_page.return_main()

    with allure.step("Переход на страницу Билеты в кино"):
        main_page.movie_tickets()
