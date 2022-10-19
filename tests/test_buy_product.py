import time
import allure

import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

@allure.description("Test select product 1")
def test_select_product_1(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    print("Start Test 1")

    login = LoginPage(driver)
    login.authorozation()

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CartPage(driver)
    cp.prouct_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    pay = PaymentPage(driver)
    pay.payment()

    fp = FinishPage(driver)
    fp.finish()

    print("Finish Test 1")
    time.sleep(3)
    driver.quit()

# @pytest.mark.run(order=1)
# def test_select_product_2(set_up):
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(chrome_options=options)
#
#     print("Start Test 2")
#
#     login = LoginPage(driver)
#     login.authorozation()
#
#     mp = MainPage(driver)
#     mp.select_products_2()
#
#     cp = CartPage(driver)
#     cp.prouct_confirmation()
#
#     print("Finish Test 2")
#     # time.sleep(3)
#     driver.quit()
#
# # @pytest.mark.run(order=2)
# def test_select_product_3():
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(chrome_options=options)
#
#     print("Start Test 3")
#
#     login = LoginPage(driver)
#     login.authorozation()
#
#     mp = MainPage(driver)
#     mp.select_products_3()
#
#     cp = CartPage(driver)
#     cp.prouct_confirmation()
#
#     print("Finish Test 3")
#     # time.sleep(3)
#     driver.quit()
