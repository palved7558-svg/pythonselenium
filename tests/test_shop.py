from pages.shop_page import ShopPage
from pages.login_page import LoginPage
from utils.demo_data import Demodata

def test_add_to_cart(setup , login , demo , shop):
    driver = setup
    login = LoginPage(driver)
    demo = Demodata(driver)
    shop = ShopPage(driver)
    driver.get(demo.url)
    driver.find_element(*login.my_account).click()
    login.login(demo.username,demo.password)
    shop.goto_shop()
    shop.add_product_to_cart("Mastering JavaScript")
