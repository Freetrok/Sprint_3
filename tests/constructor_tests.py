from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_constructor_buns(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.Constructor).click()
    driver.find_element(By.XPATH, Locators.SausesConstructor).click()
    driver.find_element(By.XPATH, Locators.BunsConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]'))
    driver.quit()

def test_constructor_sauces(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.Constructor).click()
    driver.find_element(By.XPATH, Locators.SausesConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]'))
    driver.quit()

def test_constructor_fillings(browser):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.Constructor).click()
    driver.find_element(By.XPATH, Locators.FillingsConstructor).click()
    assert EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]'))
    driver.quit()