
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

LINK_TWITTER = "https://twitter.com/home"


@pytest.fixture
def options():
    options = Options()
    # options.add_argument('--window-size=1000,800')
    options.add_argument("user-data-dir=C:/google")
    # options.add_argument('--headless')
    return options


@pytest.fixture
def driver(options) -> WebDriver:
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_change_password(driver: WebDriver):
    driver.get(LINK_TWITTER)

    try:
        wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="AppTabBar_More_Menu"]')))
        driver.find_element(By.XPATH, '//*[@data-testid="AppTabBar_More_Menu"]').click()
    except TimeoutException:
        # a = wait(driver, timeout=15).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="loginButton"]')))
        # a.click()

        wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@autocapitalize="sentences"]')))
        driver.find_element(By.XPATH, '//*[@autocapitalize="sentences"]').send_keys("sauko65@bk.ru")
        driver.find_element(By.XPATH, '//*[text()="Далее"]').click()

        wait(driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="current-password"]')))
        driver.find_element(By.XPATH, '//*[@autocomplete="current-password"]').send_keys("Lkjhgf500")
        driver.find_element(By.XPATH, '//*[@data-testid="LoginForm_Login_Button"]').click()

        wait(driver, timeout=15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="AppTabBar_More_Menu"]')))
        driver.find_element(By.XPATH, '//*[@data-testid="AppTabBar_More_Menu"]').click()

    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="settings"]')))
    driver.find_element(By.XPATH, '//*[@data-testid="settings"]').click()

    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Change your password"]')))
    driver.find_element(By.XPATH, '//*[text()="Change your password"]').click()

    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@name="current_password"]')))
    driver.find_element(By.XPATH, '//*[@name="current_password"]').send_keys("Lkjhgf500")
    driver.find_element(By.XPATH, '//*[@name="new_password"]').send_keys("Lkjhgf501")
    driver.find_element(By.XPATH, '//*[@name="password_confirmation"]').send_keys("Lkjhgf501")
    driver.find_element(By.XPATH, '//*[@data-testid="settingsDetailSave"]').click()

    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="toast"]')))
    message = driver.find_element(By.XPATH, '//*[@data-testid="toast"]').text

    assert message.startswith('Your password')


def test_random_post(driver: WebDriver) -> None:
    driver.get(LINK_TWITTER)
    driver.find_element(By.CSS_SELECTOR, '[data-testid="SideNav_NewTweet_Button"]').click()
    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="tweetTextarea_0"]')))
    driver.find_element(By.XPATH, '//*[@data-testid="tweetTextarea_0"]').send_keys("new Пост")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]').click()

    wait(driver, timeout=15).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="toast"]')))
    message = driver.find_element(By.XPATH, '//*[@data-testid="toast"]').text

    assert message.startswith('Your post')











