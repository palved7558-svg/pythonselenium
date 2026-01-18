from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Demodata:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    address = {
    "first_name": "Dipak",
    "last_name": "Palve",
    "company": "ABC Pvt Ltd",
    "email": "dipak@test.com",
    "phone": "9999999999",
    "address1": "MG Road",
    "address2": "Near Metro Station",
    "city": "Pune",
    "postcode": "411001",
    "country": "India",
    "state": "Maharashtra"
    }

    username = "palved7558@gmail.com"
    password = "Swami123@123"
    url = "https://practice.automationtesting.in/"

    