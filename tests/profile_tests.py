from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_own_cab_transit(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    assert EC.visibility_of_element_located((By.XPATH, Locators.EnterButtonLogin))


def test_own_cab_transit_logo(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    browser.find_element(By.XPATH, Locators.StellarBurgerLogo).click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton)))
    assert EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton))


def test_own_cab_transit_constructor(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.RegisterCabLine)))
    browser.find_element(By.XPATH, Locators.Constructor).click()
    assert EC.visibility_of_element_located((By.XPATH, Locators.OrderRegButton))

def test_own_cab_logout(browser, open_main_page, register):
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
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'
