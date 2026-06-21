import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

_PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _find_cached_driver(driver_name):
    wdm_cache = Path.home() / '.wdm' / 'drivers' / driver_name
    if not wdm_cache.is_dir():
        return None

    cached = sorted(
        wdm_cache.rglob(f'{driver_name}.exe'),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    return str(cached[0]) if cached else None


def _resolve_chromedriver_path():
    env_path = os.getenv('CHROMEDRIVER_PATH')
    if env_path and Path(env_path).is_file():
        return env_path

    local_driver = _PROJECT_ROOT / 'chromedriver.exe'
    if local_driver.is_file():
        return str(local_driver)

    cached = _find_cached_driver('chromedriver')
    if cached:
        return cached

    installed = ChromeDriverManager().install()
    installed_path = Path(installed)
    if installed_path.name == 'chromedriver.exe':
        return str(installed_path)

    driver_in_dir = installed_path.parent / 'chromedriver.exe'
    if driver_in_dir.is_file():
        return str(driver_in_dir)

    return installed


def _resolve_geckodriver_path():
    env_path = os.getenv('GECKODRIVER_PATH')
    if env_path and Path(env_path).is_file():
        return env_path

    local_driver = _PROJECT_ROOT / 'geckodriver.exe'
    if local_driver.is_file():
        return str(local_driver)

    cached = _find_cached_driver('geckodriver')
    if cached:
        return cached

    return GeckoDriverManager().install()


class WebdriverFactory:

    @staticmethod
    def getWebdriver(browserName):
        headless = os.getenv('HEADLESS', 'false').lower() == 'true'

        if browserName == 'firefox':
            options = FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            service = FirefoxService(_resolve_geckodriver_path())
            return webdriver.Firefox(service=service, options=options)

        if browserName == 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            service = ChromeService(_resolve_chromedriver_path())
            return webdriver.Chrome(service=service, options=options)

        raise ValueError(
            f'Неподдерживаемый браузер: {browserName}. Доступны: chrome, firefox'
        )
