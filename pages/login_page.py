from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):

    url = "https://saucedemo.com"


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    #Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("input login_button")

    # Metods
    def authorozation(self):
        """login page enter"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()

