from pages.SearchPage import SearchPage
from pages.MoviePage import MoviePage
import allure

@allure.title ("Тестирование карточки фильма")
@allure.feature ("Фильм")
@allure.description ("Тест проверяет работу параметров карточки фильма")
@allure.severity (allure.severity_level.CRITICAL)
def test_movie(browser):
    """
    Этим тестом находим фильм и заходим в его карточку
    :param browser: Webdriver - объект драйвера, переданный фикстурой
    """
    search_page = SearchPage(browser)
    with allure.step("Ввод названия фильма в поисковую строку"):
        search_page.input_movie()
    with allure.step("Выбор фильма на странице результата"):
        search_page.click_movie()

    """
    Тест находит информацию о главном актере и переходит на его страницу
    """
    movie_page = MoviePage(browser)
    with allure.step("Выбор главного актера"):
        movie_page.click_actor()
    with allure.step("Возврат на главную страницу"):
        movie_page.go_main_page()