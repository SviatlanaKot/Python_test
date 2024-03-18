from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base_page import is_visible

LINK = "https://www.google.com/intl/ru/gmail/about/"
LINK_CHANGE = "https://myaccount.google.com/u/0/security/signinoptions/password?hl=ru"


def test_create_account(driver: WebDriver):
    driver.get(LINK)
    driver.find_element(By.XPATH, '//*[@data-action="sign in"]').click()

    is_visible(driver, (By.ID, 'identifierId'))
    driver.find_element(By.ID, 'identifierId').send_keys("k.elizaveta20062016@gmail.com")
    driver.find_element(By.XPATH, '//*[text()="Далее"]').click()

    is_visible(driver, (By.XPATH, '//*[@name="Passwd"]'))
    driver.find_element(By.XPATH, '//*[@name="Passwd"]').send_keys("Zaqxsw100")
    driver.find_element(By.XPATH, '//*[text()="Далее"]').click()

    # wait(driver, 200).until(EC.url_contains('mail.google'))
    is_visible(driver, (By.CSS_SELECTOR, '[aria-label="Настройки"]'))
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Настройки"]').click()
    is_visible(driver, (By.XPATH, '//*[text()="Все настройки"]'))
    driver.find_element(By.XPATH, '//*[text()="Все настройки"]').click()

    is_visible(driver, (By.XPATH, '//*[text()="Аккаунты и импорт"]'))
    driver.find_element(By.XPATH, '//*[text()="Аккаунты и импорт"]').click()

    is_visible(driver, (By.XPATH, '//*[text()="Изменить пароль"]'))
    driver.find_element(By.XPATH, '//*[text()="Изменить пароль"]').click()

    # is_visible(driver, (By.XPATH, '//*[@name="Passwd"]'))
    # driver.find_element(By.XPATH, '//*[@name="Passwd"]').send_keys("Zaqxsw100")
    # driver.find_element(By.XPATH, '//*[text()="Далее"]').click()
    driver.get(LINK_CHANGE)

    is_visible(driver, (By.XPATH, '//*[@name="password"]'))
    driver.find_element(By.XPATH, '//*[@name="password"]').clear()
    driver.find_element(By.XPATH, '//*[@name="password"]').send_keys("Zaqxsw101")
    driver.find_element(By.XPATH, '//*[@name="confirmation_password"]').clear()
    driver.find_element(By.XPATH, '//*[@name="confirmation_password"]').send_keys("Zaqxsw101")

    sleep(10)
    driver.find_element(By.XPATH, '//*[text()="Сменить пароль"]').click()



    # assert message.startswith('')

















