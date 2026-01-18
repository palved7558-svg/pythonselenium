from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.basket_page import BasketPage
from utils.demo_data import Demodata
import time


def test_remove_from_cart(setup, login, function, demo , shop , basket):
    driver = setup
    login.go_to_login()
    login.login(demo.username , demo.password)
    shop.goto_shop()
    shop.add_product_to_cart("Mastering JavaScript")
    time.sleep(5)
    basket.goto_basket()
    basket.remove_product_from_cart("Mastering JavaScript")
