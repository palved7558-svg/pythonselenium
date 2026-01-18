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
    """Fixture to create LoginPage instance"""
    return LoginPage(setup)

@pytest.fixture
def function(setup):
    """Fixture to create Functions instance"""
    return Functions(setup)

@pytest.fixture
def demo(setup):
    """Fixture to create Demodata instance"""
    return Demodata(setup)

@pytest.fixture
def shop(setup):
    """Fixture to create Demodata instance"""
    return ShopPage(setup)

@pytest.fixture
def basket(setup):
    """Fixture to create Demodata instance"""
    return BasketPage(setup)