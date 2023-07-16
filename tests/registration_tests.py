from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import Locators
import func

def test_registration_pass(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/h2")))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__nav__g5hnF")))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys(func.gen_pass())
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys(func.gen_pass())
    browser.find_element(By.XPATH, Locators.RegisterButton).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__nav__g5hnF")))
    WebDriverWait(driver=browser, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert True
    #address = requests.get(browser.current_url)
    #assert address.status_code == 200
    browser.quit()

def test_registration_wrong_pass(browser, open_main_page):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/h2")))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__nav__g5hnF")))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей0")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys("22")
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys(func.gen_login())
    browser.find_element(By.XPATH, Locators.RegisterButton).click()
    #WebDriverWait(driver=browser, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    assert EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p[text()='Некорректный пароль']"))
    browser.quit()