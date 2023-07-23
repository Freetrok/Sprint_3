from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Locators
import func

def test_registration_pass(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.RegisterButton)))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys(func.gen_pass())
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys(func.gen_login())
    browser.find_element(By.XPATH, Locators.RegisterButton).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login' and browser.find_element(By.XPATH, Locators.EnterButtonLogin).is_displayed()


def test_registration_wrong_pass(browser):
    browser.find_element(By.XPATH, Locators.OwnCab).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.EnterButtonLogin)))
    browser.find_element(By.XPATH, Locators.RegisterButtonEnter).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, Locators.RegisterButton)))
    browser.find_element(By.XPATH, Locators.RegisterNameInput).send_keys("Сергей0")
    browser.find_element(By.XPATH, Locators.RegisterPassInput).send_keys("22")
    browser.find_element(By.XPATH, Locators.RegisterEmailInput).send_keys(func.gen_login())
    browser.find_element(By.XPATH, Locators.RegisterButton).click()
    assert browser.find_element(By.XPATH, Locators.ErrPass).is_displayed()
