from commands import *
from pages.my_account import myAccount
from pages.checkout import Checkout
from pages.shop import Shop
import time

def test_checkout_by_admin(driver, variables):
    start_testing(driver, variables)
    login = myAccount(driver, variables)
    login.login_user(driver, variables)
    # buy product
    shop = Shop(driver, variables)
    shop.buy_product(driver, variables)
    # fill checkout data
    checkout = Checkout(driver, variables)
    checkout.fill_checkout(driver, variables)
    assert checkout.check_order_details() == True

def test_checkout_by_guest(driver, variables):
    start_testing(driver, variables)
    # buy product
    shop = Shop(driver, variables)
    shop.buy_product(driver, variables)
    # fill checkout data
    checkout = Checkout(driver, variables)
    checkout.fill_checkout(driver, variables)
    assert checkout.check_order_details() == True