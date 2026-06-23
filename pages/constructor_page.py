import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from data import BUN
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Переход на вкладку «{tab_name}»')
    def click_ingredient_tab(self, tab_name):
        tabs = {
            'Булки': ConstructorPageLocators.TAB_BUNS,
            'Соусы': ConstructorPageLocators.TAB_SAUCES,
            'Начинки': ConstructorPageLocators.TAB_FILLINGS,
        }
        self.reliable_click(tabs[tab_name])

    @allure.step('Клик на ингредиент «{ingredient_name}»')
    def click_ingredient(self, ingredient_name):
        locator = self.format_locators(
            ConstructorPageLocators.INGREDIENT_BY_NAME, ingredient_name
        )
        self.reliable_click(locator)

    def _read_ingredient_counter(self, ingredient_name):
        locator = self.format_locators(
            ConstructorPageLocators.INGREDIENT_COUNTER, ingredient_name
        )
        elements = self.driver.find_elements(*locator)
        if not elements:
            return 0
        return int(elements[0].text)

    def _drag_to_constructor(self, ingredient_element, drop_zone):
        if self.driver.capabilities.get('browserName') == 'firefox':
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();
                source.dispatchEvent(
                    new DragEvent('dragstart', { bubbles: true, dataTransfer })
                );
                target.dispatchEvent(
                    new DragEvent('dragenter', { bubbles: true, dataTransfer })
                );
                target.dispatchEvent(
                    new DragEvent('dragover', { bubbles: true, dataTransfer })
                );
                target.dispatchEvent(
                    new DragEvent('drop', { bubbles: true, dataTransfer })
                );
                source.dispatchEvent(
                    new DragEvent('dragend', { bubbles: true, dataTransfer })
                );
                """,
                ingredient_element,
                drop_zone,
            )
            return

        ActionChains(self.driver).drag_and_drop(
            ingredient_element, drop_zone
        ).perform()

    @allure.step('Добавление ингредиента «{ingredient_name}» в заказ')
    def add_ingredient_to_order(self, ingredient_name):
        ingredient = self.format_locators(
            ConstructorPageLocators.INGREDIENT, ingredient_name
        )
        ingredient_element = self.wait_until_visible(ingredient)
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', ingredient_element
        )
        drop_zone = self.find_element_with_wait(
            ConstructorPageLocators.CONSTRUCTOR_DROP_ZONE
        )
        counter_before = self._read_ingredient_counter(ingredient_name)
        self._drag_to_constructor(ingredient_element, drop_zone)
        self.wait.until(
            lambda driver: self._read_ingredient_counter(ingredient_name)
            > counter_before
        )

    def _add_buns_for_order(self):
        self.click_ingredient_tab('Булки')
        # Один drag булки добавляет верхнюю и нижнюю — счётчик показывает 2
        if self.get_ingredient_counter(BUN) < 2:
            self.add_ingredient_to_order(BUN)

    @allure.step('Получение счётчика ингредиента «{ingredient_name}»')
    def get_ingredient_counter(self, ingredient_name):
        return self._read_ingredient_counter(ingredient_name)

    @allure.step('Клик на кнопку «Оформить заказ»')
    def click_order_button(self):
        self._add_buns_for_order()
        self.reliable_click(ConstructorPageLocators.ORDER_BUTTON)

    @allure.step('Закрытие модального окна ингредиента')
    def close_ingredient_modal(self):
        self.reliable_click(ConstructorPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        self.reliable_click(ConstructorPageLocators.ORDER_MODAL_CLOSE_BUTTON)

    def get_ingredient_modal_title(self):
        return self.get_text_from_element(ConstructorPageLocators.INGREDIENT_MODAL_TITLE)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(ConstructorPageLocators.INGREDIENT_MODAL)

    def wait_for_order_number(self):
        WebDriverWait(self.driver, 20).until(
            lambda driver: (
                driver.find_element(
                    *ConstructorPageLocators.ORDER_MODAL_TITLE
                ).text.isdigit()
                and driver.find_element(
                    *ConstructorPageLocators.ORDER_MODAL_TITLE
                ).text != '9999'
            )
        )

    @allure.step('Получение номера заказа из модального окна')
    def get_order_number(self):
        self.wait_for_order_number()
        return self.get_text_from_element(ConstructorPageLocators.ORDER_MODAL_TITLE)

    def is_order_modal_visible(self):
        return self.is_element_visible(ConstructorPageLocators.ORDER_MODAL)

    def is_constructor_visible(self):
        return self.is_element_visible(ConstructorPageLocators.CONSTRUCTOR_TITLE)
