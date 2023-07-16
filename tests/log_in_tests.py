from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_login_by_main_button(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.EnterAccMain).click()
    driver.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    driver.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    driver.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    driver.quit()

def test_login_by_button_in_own_cab(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.OwnCab).click()
    driver.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    driver.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    driver.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    driver.quit()

def test_login_by_button_in_reg_form(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.OwnCab).click()
    driver.find_element(By.XPATH, Locators.RegisterInLogin).click()
    driver.find_element(By.XPATH, Locators.EnterinReg).click()
    driver.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    driver.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    driver.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    driver.quit()

def test_login_by_button_in_rest_form(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.OwnCab).click()
    driver.find_element(By.XPATH, Locators.ForgotPassLogin).click()
    driver.find_element(By.XPATH, Locators.EnterinRestore).click()
    driver.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    driver.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    driver.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    driver.quit()