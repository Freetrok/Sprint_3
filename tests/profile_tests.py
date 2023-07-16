from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators

def test_own_cab_transit(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    assert EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a'))
    browser.quit()

def test_own_cab_transit_logo(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul')))
    browser.find_element(By.XPATH, Locators.StellarBurgerLogo).click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]')))
    assert EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'))
    browser.quit()

def test_own_cab_transit_constructor(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul')))
    browser.find_element(By.XPATH, Locators.Constructor).click()
    assert EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'))
    browser.quit()

def test_own_cab_logout(browser, open_main_page, register):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    browser.find_element(By.XPATH, Locators.InputFieldEmailLogin).send_keys("free@ya.ru")
    browser.find_element(By.XPATH, Locators.InputFieldPasswordLogin).send_keys("123456")
    browser.find_element(By.XPATH, Locators.EnterButtonLogin).click()
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul')))
    browser.find_element(By.XPATH, Locators.LogoutBtn).click()
    WebDriverWait(driver=browser, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    browser.quit()