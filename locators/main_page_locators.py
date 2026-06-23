from selenium.webdriver.common.by import By

class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and .//p[text()='Конструктор']]")
    FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
