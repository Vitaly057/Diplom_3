import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page = MainPage(driver)

        main_page.click_account_button()
        login_page.click_forgot_password_link()

        assert recovery_page.is_forgot_password_page_opened()
        assert recovery_page.url_matches(FORGOT_PASSWORD_URL)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_restore(self, driver, user):
        recovery_page = RecoveryPage(driver)

        recovery_page.open_forgot_password_page()
        recovery_page.enter_email(user['email'])
        recovery_page.click_restore_button()

        assert recovery_page.is_reset_password_page_opened()
        assert recovery_page.url_matches(RESET_PASSWORD_URL)
        assert recovery_page.is_save_button_visible()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_show_password_button_activates_field(self, driver, user):
        recovery_page = RecoveryPage(driver)

        recovery_page.open_forgot_password_page()
        recovery_page.enter_email(user['email'])
        recovery_page.click_restore_button()
        recovery_page.click_show_password_button()

        assert recovery_page.is_password_field_active()
