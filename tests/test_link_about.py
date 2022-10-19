# import time
# from selenium import webdriver
#
# from base.base_class import Base
# from pages.cart_page import CartPage
# from pages.client_information_page import ClientInformationPage
# from pages.finish_page import FinishPage
# from pages.login_page import LoginPage
# from selenium.webdriver.chrome.options import Options
# from pages.main_page import MainPage
# from pages.payment_page import PaymentPage
#
#
# class BaseClass:
#     pass
#
#
# def test_link_about():
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(chrome_options=options)
#
#     print("Start Test")
#
#     login = LoginPage(driver)
#     login.authorozation()
#
#     mp = MainPage(driver)
#     mp.select_menu_about()
#
#
#
#
#
#     print("Finish test")
#     time.sleep(10)
#     driver.quit()
#
#
