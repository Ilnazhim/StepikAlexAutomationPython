import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utilities.logger import Logger

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope="module")
def set_group():

    print("Enter system")
    yield
    print("Exit system")



