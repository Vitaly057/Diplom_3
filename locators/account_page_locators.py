from selenium.webdriver.common.by import By
class AccountPageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_NUMBER_IN_HISTORY = (
        By.XPATH,
        "//li[contains(@class, 'OrderHistory_listItem')]"
        "//p[contains(@class, 'text_type_digits-default')]",
    )
