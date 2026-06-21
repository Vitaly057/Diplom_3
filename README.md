# Diplom_3 — UI-тесты Stellar Burgers

# О чём проект
Автотесты для учебного сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/).
Проверяю восстановление пароля, личный кабинет, конструктор бургера и ленту заказов.

# Что проверяют тесты
- переход на восстановление пароля, ввод email, показ и скрытие пароля
- личный кабинет: переход, история заказов, выход из аккаунта
- конструктор: навигация, попап ингредиента, счётчик, оформление заказа авторизованным пользователем
- лента заказов: попап заказа, счётчики «Выполнено за всё время» и «Выполнено за сегодня», заказ в работе

# Как запустить
1. Создать venv и установить зависимости (если папка `venv` уже есть — создание можно пропустить, достаточно активировать):
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Запустить все тесты в Chrome:
   `pytest --browser=chrome --alluredir=allure-results`

3. Запустить в Firefox:
   `pytest --browser=firefox --alluredir=allure-results`

4. Запуск без окна браузера — перед pytest выставить `HEADLESS=true`:
   `set HEADLESS=true` (Windows) или `export HEADLESS=true` (Linux/macOS)

5. Запустить один файл, например:
   `pytest tests/test_main_functionality.py -v --browser=chrome`

6. Allure-отчёт:
   `allure serve allure-results`

# Структура проекта
- `locators/` — локаторы страниц
- `pages/` — Page Object
- `tests/` — тесты по разделам (конструктор, лента, пароль, личный кабинет)
- `factories/` — запуск Chrome и Firefox
- `helpers/` — регистрация и удаление пользователя через API
- `conftest.py` — фикстуры pytest (driver, user, logged_in_driver)
- `config.py` — URL API
- `data.py` — тестовые данные
- `urls.py` — адреса страниц
- `pytest.ini`
- `requirements.txt`

# Какие технологии использовал
- Python 3.12
- Selenium WebDriver + webdriver-manager
- pytest
- Allure
- Page Object Model
- requests (API `https://stellarburgers.education-services.ru/api`)

# Примечание
Тестовые пользователи создаются через API перед тестом и удаляются после него.
UI открывается на `https://stellarburgers.education-services.ru/` — адрес можно переопределить через переменную `BASE_URL`.
Каждый тест поднимает свой браузер. Драйверы подтягиваются через webdriver-manager или берутся из кэша `~/.wdm`.
