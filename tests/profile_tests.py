from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_own_cab_transit(browser, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    assert browser.find_element(By.XPATH, Locators.EnterButtonLogin).is_displayed()

def test_own_cab_registered_transit(browser, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and browser.find_element(By.XPATH, Locators.RegisterCabLine).is_displayed()

def test_own_cab_transit_logo(browser, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    browser.find_element(By.XPATH, Locators.StellarBurgerLogo).click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/' and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()


def test_own_cab_transit_constructor(browser, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    browser.find_element(By.XPATH, Locators.Constructor).click()
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/' and browser.find_element(By.XPATH, Locators.OrderRegButton).is_displayed()


def test_own_cab_logout(browser, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    browser.find_element(By.XPATH, Locators.LogoutBtn).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login' and browser.find_element(By.XPATH, Locators.EnterButtonLogin).is_displayed()
