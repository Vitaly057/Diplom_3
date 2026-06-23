import allure
import pytest
from data import FILLING
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('При клике на заказ открывается всплывающее окно с деталями')
    def test_order_details_popup(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_feed_button()
        order_feed_page.click_first_order()

        assert order_feed_page.is_order_modal_visible()
        assert order_feed_page.get_order_modal_number().startswith('#')

    @allure.title('Заказы из «Истории заказов» отображаются в «Ленте заказов»')
    def test_order_from_history_appears_in_feed(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        constructor_page = ConstructorPage(logged_in_driver)
        account_page = AccountPage(logged_in_driver)
        order_feed_page = OrderFeedPage(logged_in_driver)

        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.add_ingredient_to_order(FILLING)
        constructor_page.click_order_button()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal()

        main_page.click_account_button()
        account_page.click_order_history_link()
        assert account_page.is_order_in_history(order_number)

        main_page.click_feed_button()
        assert order_feed_page.is_order_in_feed(order_number)

    @allure.title('При создании заказа увеличивается счётчик «Выполнено за {counter_label}»')
    @pytest.mark.parametrize(
        'counter_type, counter_label',
        [
            ('total', 'все время'),
            ('today', 'сегодня'),
        ],
    )
    def test_orders_counter_increases(self, logged_in_driver, counter_type, counter_label):
        main_page = MainPage(logged_in_driver)
        constructor_page = ConstructorPage(logged_in_driver)
        order_feed_page = OrderFeedPage(logged_in_driver)

        main_page.click_feed_button()
        counter_before = order_feed_page.get_orders_counter(counter_type)

        main_page.click_constructor_button()
        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.add_ingredient_to_order(FILLING)
        constructor_page.click_order_button()
        constructor_page.get_order_number()
        constructor_page.close_order_modal()

        main_page.click_feed_button()
        counter_after = order_feed_page.get_orders_counter(counter_type)

        assert counter_after > counter_before

    @allure.title('После оформления заказа номер появляется в разделе «В работе»')
    def test_order_number_appears_in_progress_section(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        constructor_page = ConstructorPage(logged_in_driver)
        order_feed_page = OrderFeedPage(logged_in_driver)

        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.add_ingredient_to_order(FILLING)
        constructor_page.click_order_button()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal()

        main_page.click_feed_button()
        order_in_progress = order_feed_page.get_order_number_in_progress()

        assert order_number in order_in_progress
