import allure
from pages.SearchPage import SearchPage


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

    with allure.step("Ввод названия фильма в поисковую строку"):
        search_page.input_movie()

    with allure.step("Выбор фильма на странице результата"):
        search_page.click_movie()



