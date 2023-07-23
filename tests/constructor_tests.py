from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_constructor_buns(browser):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.SausesConstructor).click()
    browser.find_element(By.XPATH, Locators.BunsConstructor).click()
    assert browser.find_element(By.XPATH, Locators.BunsList).is_displayed()

def test_constructor_sauces(browser):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.SausesConstructor).click()
    assert browser.find_element(By.XPATH, Locators.SausesList).is_displayed()

def test_constructor_fillings(browser):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.FillingsConstructor).click()
    assert browser.find_element(By.XPATH, Locators.FillingsList).is_displayed()
