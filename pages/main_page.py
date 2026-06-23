import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL, FEED_URL


class MainPage(BasePage):

    @allure.step('Клик на «Личный кабинет»')
    def click_account_button(self):
        self.reliable_click(MainPageLocators.ACCOUNT_BUTTON)
        self.wait.until(
            lambda driver: '/account' in driver.current_url
            or '/login' in driver.current_url
        )

    @allure.step('Клик на «Конструктор»')
    def click_constructor_button(self):
        self.reliable_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на «Лента заказов»')
    def click_feed_button(self):
        self.reliable_click(MainPageLocators.FEED_BUTTON)

    def is_constructor_page_opened(self):
        return self.get_current_url() == BASE_URL

    def is_feed_page_opened(self):
        return self.get_current_url() == FEED_URL
