import allure
from pages.SearchPage import SearchPage
from pages.MainPage import MainPage
from pages.CinemaPage import CinemaPage

@allure.title ("Тестирование поиска фильма")
@allure.feature ("Поиск")
@allure.description ("Тест проверяет корректность поисковой строки")
@allure.severity (allure.severity_level.CRITICAL)
def test_search_movie(browser):
    """
    Тест проверяет работу поисковой строки
    :param browser: Webdriver - объект драйвера, переданный фикстурой
    """
    search_page = SearchPage(browser)
    with allure.step("Открытие сайта Кинопоиск"):
        search_page.open()

    with allure.step("Ввод названия фильма в поисковую строку"):
        search_page.input_movie()

    with allure.step("Выбор фильма на странице результата"):
        search_page.click_movie()

    with allure.step("Возврат на главную страницу"):
        search_page.go_main_page()

@allure.title("Тестирование главной страницы")
@allure.feature("Кинопоиск")
@allure.description("Тест проверяет работу кнопок, иконок на главной странице")
@allure.severity(allure.severity_level.CRITICAL)
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

    with allure.step("Переход на страницу Спорт"):
        main_page.sport()



@allure.title("Тестирование Онлайн-кинотеатра")
@allure.feature("Онлайн-кинотеатр")
@allure.description("Тест проверяет работу кнопок, иконок на странице Онлайн-кинотеатра")
@allure.severity(allure.severity_level.CRITICAL)
def test_cinema(browser):
    """
    Тест проверяет переходы при нажатии на кнопки, иконки, логотипы
    :param browser: Webdriver - объект драйвера, переданный фикстурой
    """
    cinema_page = CinemaPage(browser)
    with allure.step("Открывает сайт Кинопоиск"):
        cinema_page.open()
    with allure.step("Открывает Онлайн_кинотеатр"):
        cinema_page.online_cinema()

    with allure.step("Переход на страницу Каналы"):
        cinema_page.icon_channels()

    with allure.step("Выбор каналов"):
        cinema_page.watch_childrens()






