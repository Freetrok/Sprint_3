from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_login_by_main_button(browser):
    browser.find_element(By.XPATH, Locators.EnterAccMain).click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, Locators.MenuLine)))
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()

def test_login_by_button_in_own_cab(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()

def test_login_by_button_in_reg_form(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.RegisterInLogin).click()
    browser.find_element(By.XPATH, Locators.EnterinReg).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/' and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()


def test_login_by_button_in_rest_form(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.ForgotPassLogin).click()
    browser.find_element(By.XPATH, Locators.EnterinRestore).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("sep@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/' and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()
