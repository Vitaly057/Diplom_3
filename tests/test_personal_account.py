import allure
from pages.account_page import AccountPage
from pages.main_page import MainPage
from urls import ACCOUNT_URL, LOGIN_URL, ORDER_HISTORY_URL

@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Переход в личный кабинет по клику на «Личный кабинет»')
    def test_transition_to_personal_account(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        account_page = AccountPage(logged_in_driver)

        main_page.click_account_button()

        assert account_page.is_profile_page_opened()
        assert logged_in_driver.current_url.rstrip('/') in {
            ACCOUNT_URL.rstrip('/'),
            f'{ACCOUNT_URL.rstrip("/")}/profile',
        }

    @allure.title('Переход в раздел «История заказов»')
    def test_transition_to_order_history(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        account_page = AccountPage(logged_in_driver)

        main_page.click_account_button()
        account_page.click_order_history_link()

        assert account_page.is_order_history_page_opened()
        assert logged_in_driver.current_url == ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта по кнопке «Выход»')
    def test_logout_from_account(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        account_page = AccountPage(logged_in_driver)

        main_page.click_account_button()
        account_page.click_logout_button()

        assert account_page.is_login_page_opened()
        assert logged_in_driver.current_url == LOGIN_URL
