from time import sleep
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import seleniumwire.undetected_chromedriver as uc


@pytest.fixture
def options():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-data-dir=C:/google")
    # options.add_argument('--headless')
    return options


@pytest.fixture
def driver(options) -> WebDriver:
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = uc.Chrome(
        options=chrome_options,
        seleniumwire_options={}
    )

    yield driver
    driver.quit()
