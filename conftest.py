import os
import pytest
from factories.web_driver_factory import WebdriverFactory
from helpers.user import delete_user, register_user
from pages.login_page import LoginPage
from urls import BASE_URL

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default=os.getenv('BROWSER', 'chrome'),
        help='Браузер для запуска тестов: chrome или firefox',
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('--browser')
    browser = WebdriverFactory.getWebdriver(browser_name)

    width = int(os.getenv('BROWSER_WIDTH', '1920'))
    height = int(os.getenv('BROWSER_HEIGHT', '1080'))
    browser.set_window_size(width, height)
    browser.get(os.getenv('BASE_URL', BASE_URL))

    yield browser
    browser.quit()

@pytest.fixture
def user():
    response, payload = register_user()
    assert response.status_code == 200, response.text
    access_token = response.json()['accessToken']

    yield {
        'email': payload['email'],
        'password': payload['password'],
        'name': payload['name'],
        'accessToken': access_token,
    }

    delete_user(access_token)

@pytest.fixture
def logged_in_driver(driver, user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user['email'], user['password'])
    yield driver
