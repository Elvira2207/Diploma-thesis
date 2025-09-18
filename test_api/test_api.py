import pytest
import requests
import allure


BASE_URL = "https://api.kinopoisk.dev/v1.4/movie"
api_token = "" #В сопроводительном письме

@allure.title ("Поиск по названию фильма")
@allure.description("Тест проверяет корректность поисковой строки с позитивным параметром")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_title_positive():
    with allure.step("Ввод названия фильма"):
        payload = {
        "type":"searchRequest",
        "id":"Лёд"
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка GET запроса"):
        resp = requests.get(BASE_URL, json=payload, headers=headers)
    with allure.step("Проверка код ответа 200"):
        assert resp.status_code == 200

@allure.title ("Поиск по жанру и году выпуска")
@allure.description("Тест проверяет корректность поисковой строки с позитивным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_genre_positive():
    with allure.step("Ввод названия жанра и года выпуска"):
        params = {
        "year": 2024,
        "genres.name": "криминал"
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка GET запроса"):
        resp = requests.get(BASE_URL, params=params, headers=headers)
    with allure.step("Проверка код ответа 200"):
        assert resp.status_code == 200

@allure.title ("Поиск по рейтингу")
@allure.description("Тест проверяет корректность поисковой строки с позитивным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_rating_positive():
    with allure.step("Ввод рейтинга фильма"):
        params = {
        "ratings": 8,
        "genres.name": "спорт"
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка GET запроса"):
        resp = requests.get(BASE_URL, params=params, headers=headers)
    with allure.step("Проверка код ответа 200"):
        assert resp.status_code == 200

@allure.title ("Поиск по произвольному набору")
@allure.description("Тест проверяет корректность поисковой строки с негативным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_random_letters_negative():
    with allure.step("Ввод произвольного набора букв, символов"):
        payload = {
        "type": "searchRequest",
        "id": "Rbvbiyfz"
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка GET запроса"):
        resp = requests.get(BASE_URL, json=payload, headers=headers)
    with allure.step("Проверка код ответа 200"):
        assert resp.status_code == 200

@allure.title ("Поиск по набору со спецсимволами")
@allure.description("Тест проверяет корректность поисковой строки с негативным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_specsymbol_negative():
    with allure.step("Ввод произвольного набора букв, символов"):
        params = {
        "ratings": "!@#$%^",
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка GET запроса"):
        resp = requests.get(BASE_URL, params=params, headers=headers)
    with allure.step("Проверка код ответа 200"):
        assert resp.status_code == 200

@allure.title ("Поиск с другим методом отправки")
@allure.description("Тест проверяет корректность поисковой строки с негативным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_other_method_negative():
    with allure.step("Ввод параметров поиска"):
        params = {
        "year": 2024,
        "genres.name": "криминал"
        }
    with allure.step("Ввод заголовка"):
        headers = {
        "X-API-KEY": api_token
        }
    with allure.step("Отправка POST запроса"):
        resp = requests.post(BASE_URL, params=params, headers=headers)
    with allure.step("Проверка код ответа 404"):
        assert resp.status_code == 404

@allure.title ("Поиск без токена")
@allure.description("Тест проверяет корректность поисковой строки с негативным параметром ")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_without_token_negative():
    with allure.step("Ввод параметров"):
        params = {
        "ratings": "9-10",
        }
    with allure.step("Убираем с заголовка токен"):
        headers = {
        }
    with allure.step("Отправка POST запроса"):
        resp = requests.get(BASE_URL, params=params, headers=headers)
    with allure.step("Проверка код ответа 401"):
        assert resp.status_code == 401
