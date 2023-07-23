import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver
    driver.quit()

@pytest.fixture()
def register(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.RegisterButton)))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys("123456")
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.RegisterButton).click()





