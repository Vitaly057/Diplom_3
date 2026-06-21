import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def format_locators(self, locator, value):
        method, selector = locator
        return method, selector.format(value)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_invisible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find_element_with_wait(self, locator):
        return self.wait_until_visible(locator)

    def reliable_click(self, locator):
        element = self.wait_until_clickable(locator)
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element
        )
        try:
            element.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', element)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Заполнение поля текстом')
    def send_keys_to_element(self, locator, text):
        element = self.wait_until_clickable(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except TimeoutException:
            return False
