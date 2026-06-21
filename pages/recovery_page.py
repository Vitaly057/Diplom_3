import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class RecoveryPage(BasePage):

    @allure.step('Открытие страницы восстановления пароля')
    def open_forgot_password_page(self):
        self.open(FORGOT_PASSWORD_URL)

    @allure.step('Ввод email для восстановления пароля')
    def enter_email(self, email):
        self.send_keys_to_element(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик на кнопку «Восстановить»')
    def click_restore_button(self):
        self.reliable_click(RecoveryPageLocators.RESTORE_BUTTON)
        self.wait.until(
            lambda driver: driver.current_url.rstrip('/') == RESET_PASSWORD_URL.rstrip('/')
        )

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_show_password_button(self):
        self.reliable_click(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    def is_forgot_password_page_opened(self):
        return self.get_current_url().rstrip('/') == FORGOT_PASSWORD_URL.rstrip('/')

    def is_reset_password_page_opened(self):
        return self.get_current_url().rstrip('/') == RESET_PASSWORD_URL.rstrip('/')

    def is_save_button_visible(self):
        return self.is_element_visible(RecoveryPageLocators.SAVE_BUTTON)

    def is_password_field_active(self):
        return self.is_element_visible(RecoveryPageLocators.ACTIVE_PASSWORD_FIELD)
