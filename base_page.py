
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.wait import WebDriverWait


def is_visible(driver, locator):
    return wait(driver, timeout=50).until(EC.visibility_of_element_located(locator))


def is_clickable(driver, locator):
    return wait(driver, timeout=30).until(EC.element_to_be_clickable(locator))

