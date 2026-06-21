import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Клик на первый заказ в ленте')
    def click_first_order(self):
        self.reliable_click(OrderFeedPageLocators.FIRST_ORDER_IN_FEED)

    @allure.step('Получение счётчика «{counter_type}»')
    def get_orders_counter(self, counter_type):
        locators = {
            'total': OrderFeedPageLocators.TOTAL_ORDERS_COUNTER,
            'today': OrderFeedPageLocators.TODAY_ORDERS_COUNTER,
        }
        return int(self.get_text_from_element(locators[counter_type]))

    def is_order_modal_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL)

    def get_order_modal_number(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_MODAL_NUMBER)

    @allure.step('Проверка наличия заказа {order_number} в ленте')
    def is_order_in_feed(self, order_number):
        locator = self.format_locators(
            OrderFeedPageLocators.ORDER_NUMBER_BY_TEXT, order_number
        )
        self.wait.until(EC.presence_of_element_located(locator))
        return True

    @allure.step('Получение номера заказа из раздела «В работе»')
    def get_order_number_in_progress(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_NUMBER_IN_PROGRESS)

    def is_feed_page_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.FEED_TITLE)
