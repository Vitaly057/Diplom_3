from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    FEED_TITLE = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]/h1")
    FIRST_ORDER_IN_FEED = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]")
    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_orderBox')]",
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_orderBox')]"
        "//p[contains(@class, 'text_type_digits-default')]",
    )
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    ORDER_NUMBER_IN_PROGRESS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList') and not(contains(@class, 'Ready'))]/li",
    )
    ORDER_NUMBER_BY_TEXT = (
        By.XPATH,
        "//li[contains(@class, 'OrderHistory_listItem')]"
        "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{0}')]",
    )
