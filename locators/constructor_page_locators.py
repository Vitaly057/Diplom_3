from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'BurgerIngredients_ingredients')]/h1",
    )
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    INGREDIENT_BY_NAME = (
        By.XPATH,
        "//p[text()='{0}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]",
    )
    INGREDIENT = (
        By.XPATH,
        "//p[text()='{0}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]",
    )
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[text()='{0}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]"
        "//p[contains(@class, 'counter_counter__num')]",
    )
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_modal__container')]",
    )
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2",
    )
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'close')]",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_modal__container')]",
    )
    ORDER_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2",
    )
    ORDER_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'close')]",
    )
