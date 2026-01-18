from multiprocessing.spawn import import_main_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.functions import Functions
import time
from utils.demo_data import Demodata
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.function = Functions(driver)
        self.demo = Demodata(driver)

    my_account = (By.CSS_SELECTOR, "#main-nav a[href*='my-account']")
    reg_email_address = (By.CSS_SELECTOR, "[id='reg_email']")
    reg_password = (By.CSS_SELECTOR, "[id='reg_password']")
    reg_btn = (By.CSS_SELECTOR, "[name='register']")
    log_email_address = (By.CSS_SELECTOR, "[id='username']")
    log_password = (By.CSS_SELECTOR, "[id='password']")
    log_btn = (By.CSS_SELECTOR, "[name='login']")
    addresses = (By.XPATH , "//a[contains(text(),'Addresses')]")
    billing_address = (By.XPATH , "//*[contains(@href,'/edit-address/bill')]")
    shipping_address = (By.XPATH , "//*[contains(@href,'/edit-address/ship')]")
    bill_first_name = (By.CSS_SELECTOR , "[name='billing_first_name']")
    bill_last_name = (By.CSS_SELECTOR , "[name='billing_last_name']")
    bill_compnay_name = (By.CSS_SELECTOR , "[name='billing_company']")
    bill_email = (By.CSS_SELECTOR , "[name='billing_email']")
    bill_phone = (By.CSS_SELECTOR , "[name='billing_phone']")
    bill_address_line1 = (By.CSS_SELECTOR , "[name='billing_address_1']")
    bill_address_line2 = (By.CSS_SELECTOR , "[name='billing_address_2']")
    bill_city = (By.CSS_SELECTOR , "[name='billing_city']")
    bill_postcode = (By.CSS_SELECTOR , "[name='billing_postcode']")
    country_dropdown = (By.CSS_SELECTOR , "#s2id_billing_country")
    state_dropdown = (By.CSS_SELECTOR , "#s2id_billing_state")
    dp_input = (By.CSS_SELECTOR , "#select2-drop input")
    dp_input_list = (By.CSS_SELECTOR , "#select2-drop li")
    bill_save_button = (By.CSS_SELECTOR , "[name='save_address']")
    saved_address = (By.XPATH , "(//address)[1]")
    errormsg = (By.XPATH, "//strong[text()='Error:']")



    def login(self, user, pwd):
        self.driver.find_element(*self.log_email_address).send_keys(self.demo.username)
        self.driver.find_element(*self.log_password).send_keys(self.demo.password)
        self.driver.find_element(*self.log_btn).click()

    def go_to_login(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')

    def verify_registration(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Error:']")))
            print("user already exists")
        except TimeoutException:
            print("registration successful or no error shown")

    def verify_login(self):
        try:
            assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Sign out']")))
            print("login successful")
        except TimeoutException:
            print("login failed")

    def verify_address(self , address):
        address_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.saved_address)).text
        assert address["company"] in address_text
        assert f"{address['first_name']} {address['last_name']}" in address_text
        assert address["address1"] in address_text
        assert address["address2"] in address_text
        assert f"{address['city']} - {address['postcode']}" in address_text
        assert address["state"] in address_text


    def select_dropdown_by_text(self ,driver, text):
        wait = WebDriverWait(driver, 10)

        options = wait.until(
        EC.presence_of_all_elements_located(self.dp_input_list)
        )

        for option in options:
            if option.text.strip() == text:
                self.function.click_element_safe(option)
                break

    def address_update(self, type, address):
        if type == "billing":
            self.function.click_element_safe(self.billing_address)
            self.function.send_keys_safe(self.bill_first_name, address["first_name"])
            self.function.send_keys_safe(self.bill_last_name, address["last_name"])
            self.function.send_keys_safe(self.bill_compnay_name, address["company"])
            self.function.send_keys_safe(self.bill_email, address["email"])
            self.function.send_keys_safe(self.bill_phone, address["phone"])
            self.function.send_keys_safe(self.bill_address_line1, address["address1"])
            self.function.send_keys_safe(self.bill_address_line2, address["address2"])
            self.function.send_keys_safe(self.bill_city, address["city"])
            self.function.send_keys_safe(self.bill_postcode, address["postcode"])
            self.function.click_element_safe(self.country_dropdown)
            self.function.send_keys_safe(self.dp_input, address["country"])
            self.select_dropdown_by_text(self.driver , address["country"] )
            self.function.scroll_element_to_center(self.state_dropdown)
            self.function.click_element_safe(self.state_dropdown)
            self.function.send_keys_safe(self.dp_input, address["state"])
            self.select_dropdown_by_text(self.driver , address["state"] )
            self.function.click_element_safe(self.bill_save_button)

        elif type == "shipping":
            self.function.click_element_safe(self.shipping_address)

        else:
            raise ValueError("Invalid address type: use 'billing' or 'shipping'")





