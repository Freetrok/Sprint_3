import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators
import func
import Locators


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    yield driver
    driver.quit()

@pytest.fixture()
def open_main_page(browser):
    browser.get('https://stellarburgers.nomoreparties.site/')

@pytest.fixture()
def register(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/h2")))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__nav__g5hnF")))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys("123456")
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.RegisterButton).click()



