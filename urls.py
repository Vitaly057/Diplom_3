import os

BASE_URL = os.getenv('BASE_URL', 'https://stellarburgers.education-services.ru/')
if not BASE_URL.endswith('/'):
    BASE_URL += '/'

LOGIN_URL = f'{BASE_URL}login'
FORGOT_PASSWORD_URL = f'{BASE_URL}forgot-password'
RESET_PASSWORD_URL = f'{BASE_URL}reset-password'
FEED_URL = f'{BASE_URL}feed'
ACCOUNT_URL = f'{BASE_URL}account'
ORDER_HISTORY_URL = f'{BASE_URL}account/order-history'
