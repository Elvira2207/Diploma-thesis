import requests


BASE_URL = "https://api.kinopoisk.dev/v1.4/movie"


def test_search_title_positive():
    payload = {
        "type":"searchRequest",
        "id":"Лёд"
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.get(BASE_URL, json=payload, headers=headers)
    assert resp.status_code == 200

def test_search_genre_positive():
    params = {
        "year": 2024,
        "genres.name": "криминал"
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.get(BASE_URL, params=params, headers=headers)
    assert resp.status_code == 200

def test_search_rating_positive():
    params = {
        "ratings": 8,
        "genres.name": "спорт"
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.get(BASE_URL, params=params, headers=headers)
    assert resp.status_code == 200

def test_search_random_letters_negative():
    payload = {
        "type": "searchRequest",
        "id": "Rbvbiyfz"
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.get(BASE_URL, json=payload, headers=headers)
    assert resp.status_code == 200

def test_search_specsymbol_negative():
    params = {
        "ratings": "!@#$%^",
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.get(BASE_URL, params=params, headers=headers)
    assert resp.status_code == 200

def test_search_other_method_negative():
    params = {
        "year": 2024,
        "genres.name": "криминал"
    }
    headers = {
        "X-API-KEY": api_token
    }
    resp = requests.post(BASE_URL, params=params, headers=headers)
    assert resp.status_code == 404

def test_search_without_token_negative():
    params = {
        "ratings": "9-10",
    }
    headers = {
    }
    resp = requests.get(BASE_URL, params=params, headers=headers)
    assert resp.status_code == 401
