# Дипломный проект по автоматизации тестирования сайта «Кинопоиск

## Установка необходимых технологий

1. **Python**: Основной язык программирования для написания тестов.
2. **Selenium**: Библиотека для автоматизации взаимодействия с веб-браузером.
3. **Pytest**: Фреймворк для написания и запуска тестов.
4. **Allure**: Инструмент для генерации отчетов о выполнении тестов.
5. **Браузеры Google Chrome**
   
### Шаги

1. Склонировать репозиторий:
 git clone https://github.com/Elvira2207/Diploma-thesis.git

2. Установить зависимости :
- pip install -r requirements.txt
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest

3. Запустить тесты 'pytest':
# Все тесты
pytest 
# Только UI тесты
pytest -m ui
# Только API тесты
pytest -m api
# С генерацией отчета Allure
pytest –alluredir allure-result

### Структура

**conftest.py**: 
Фикстура pytest - Инициализация браузера для UI тестов
**test_api.py**: 
API тесты 
**test_ui.py**: 
UI тесты с использованием Page Object
**requirements.txt**: 
Список всех зависимостей проекта для установки через pip
**README.md**: 
Документация
**gitignore**: 
Игнорируемые файлы

### Важные команды

# Проверка кода на соответствие PEP8
flake8 .
# Запуск тестов с отчетом Allure
pytest --alluredir=allure-results
# Просмотр отчета Allure
allure serve allure-results









