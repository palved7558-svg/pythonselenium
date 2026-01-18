import time

def test_registration(setup, login, function, demo):
    driver = setup
    driver.get(demo.url)
    driver.find_element(*login.my_account).click()
    driver.find_element(*login.reg_email_address).send_keys(demo.username)
    driver.find_element(*login.reg_password).send_keys(demo.password)
    function.click_element_safe(login.reg_btn)
    login.verify_registration()

def test_login_valid(setup, login , demo):
    driver = setup
    driver.get(demo.url)
    driver.find_element(*login.my_account).click()
    login.login(demo.username, demo.password)
    login.verify_login()


def test_address_update(setup, login, function, demo):
    driver = setup
    driver.get(demo.url)
    driver.find_element(*login.my_account).click()
    login.login(demo.username, demo.password)
    function.click_element_safe(login.addresses)
    login.address_update("billing", demo.address)
    function.click_element_safe(login.addresses)
    login.verify_address(demo.address)


    



