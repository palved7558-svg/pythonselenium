from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.functions import Functions



class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.functions = Functions(driver)

    my_account = (By.CSS_SELECTOR, "#main-nav a[href*='my-account']")
    shop = (By.CSS_SELECTOR, "#main-nav a[href*='shop']")
    

    def add_to_cart_btn(self, product_name):
        return (
            By.XPATH,
            f"//h3[text()='{product_name}']/ancestor::li//a[contains(@class,'add_to_cart_button')]"
        )
    

    def goto_shop(self):
        self.driver.get("https://practice.automationtesting.in/shop/")

    def add_product_to_cart(self, product_name):
        locator = self.add_to_cart_btn(product_name)
        self.functions.click_element_safe(locator)
        
    