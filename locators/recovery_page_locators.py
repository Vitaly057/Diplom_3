from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]",
    )
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH,
        "//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]",
    )
