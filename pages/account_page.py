import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from urls import ACCOUNT_URL, LOGIN_URL, ORDER_HISTORY_URL


class AccountPage(BasePage):

    @allure.step('Клик на «История заказов»')
    def click_order_history_link(self):
        self.reliable_click(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step('Клик на кнопку «Выход»')
    def click_logout_button(self):
        self.reliable_click(AccountPageLocators.LOGOUT_BUTTON)
        self.wait.until(
            lambda driver: driver.current_url.rstrip('/') == LOGIN_URL.rstrip('/')
        )

    def is_profile_page_opened(self):
        current_url = self.get_current_url().rstrip('/')
        return current_url in {
            ACCOUNT_URL.rstrip('/'),
            f'{ACCOUNT_URL.rstrip("/")}/profile',
        }

    def is_order_history_page_opened(self):
        return self.get_current_url().rstrip('/') == ORDER_HISTORY_URL.rstrip('/')

    def is_login_page_opened(self):
        return self.get_current_url().rstrip('/') == LOGIN_URL.rstrip('/')

    @allure.step('Проверка наличия заказа {order_number} в истории')
    def is_order_in_history(self, order_number):
        self.wait.until(
            lambda driver: any(
                order_number in number.text
                for number in driver.find_elements(
                    *AccountPageLocators.ORDER_NUMBER_IN_HISTORY
                )
            )
        )
        return True
