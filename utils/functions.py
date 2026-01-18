from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Functions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def send_keys_safe(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def scroll_element_to_center(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest'});",
            element
        )

    def click_element_safe(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        
        try:
            element.click()
        except Exception:
            # Fallback: Scroll into view and use JavaScript click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
