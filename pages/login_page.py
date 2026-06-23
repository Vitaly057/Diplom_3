import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, LOGIN_URL


class LoginPage(BasePage):

    @allure.step('Открытие страницы входа')
    def open_login_page(self):
        self.open(LOGIN_URL)

    @allure.step('Авторизация пользователя')
    def login(self, email, password):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.reliable_click(LoginPageLocators.LOGIN_BUTTON)
        self.wait.until(
            lambda driver: driver.current_url.rstrip('/') == BASE_URL.rstrip('/')
        )

    @allure.step('Клик на «Восстановить пароль»')
    def click_forgot_password_link(self):
        self.reliable_click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def is_login_page_opened(self):
        return self.get_current_url() == LOGIN_URL
