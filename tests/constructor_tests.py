from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_constructor_buns(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.SausesConstructor).click()
    browser.find_element(By.XPATH, Locators.BunsConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, Locators.BunsLiat))

def test_constructor_sauces(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.SausesConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, Locators.SausesList))

def test_constructor_fillings(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.Constructor).click()
    browser.find_element(By.XPATH, Locators.FillingsConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, Locators.FillingsList))
