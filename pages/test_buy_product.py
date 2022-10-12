import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

def test_select_product():
    options = Options()
    driver = webdriver.Chrome()

    print("Start Test")


    login = LoginPage(driver)
    login.authorozation()

    select_product = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))).click()
    print("Click select product")

    enter_shoping_card = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']"))).click()
    print("Click Enter Shoping Cart")

    success_test = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='title']"))).text

    assert success_test == "YOUR CART"
    print("Test success")

    time.sleep(10)



