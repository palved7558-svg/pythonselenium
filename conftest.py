import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils.functions import Functions
from utils.demo_data import Demodata
from pages.shop_page import ShopPage
from pages.basket_page import BasketPage

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(setup):
    return LoginPage(setup)

@pytest.fixture
def function(setup):
    return Functions(setup)

@pytest.fixture
def demo(setup):
    return Demodata(setup)

@pytest.fixture
def shop(setup):
    return ShopPage(setup)

@pytest.fixture
def basket(setup):
    return BasketPage(setup)