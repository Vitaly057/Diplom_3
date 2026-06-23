import allure
from data import FILLING
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_transition_to_constructor(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.click_feed_button()
        main_page.click_constructor_button()

        assert main_page.is_constructor_page_opened()
        assert constructor_page.is_constructor_visible()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_transition_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_feed_button()

        assert main_page.is_feed_page_opened()
        assert order_feed_page.is_feed_page_visible()

    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_ingredient_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.click_ingredient(FILLING)

        assert constructor_page.is_ingredient_modal_visible()
        assert constructor_page.get_ingredient_modal_title() == 'Детали ингредиента'

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.click_ingredient(FILLING)
        constructor_page.close_ingredient_modal()

        assert not constructor_page.is_ingredient_modal_visible()

    @allure.title('При добавлении ингредиента увеличивается счётчик')
    def test_ingredient_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.click_ingredient_tab('Начинки')
        counter_before = constructor_page.get_ingredient_counter(FILLING)
        constructor_page.add_ingredient_to_order(FILLING)
        counter_after = constructor_page.get_ingredient_counter(FILLING)

        assert counter_after > counter_before

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, logged_in_driver):
        constructor_page = ConstructorPage(logged_in_driver)

        constructor_page.click_ingredient_tab('Начинки')
        constructor_page.add_ingredient_to_order(FILLING)
        constructor_page.click_order_button()

        assert constructor_page.is_order_modal_visible()
        order_number = constructor_page.get_order_number()
        assert order_number.isdigit()
