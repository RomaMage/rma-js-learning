from commands import *
from pages.shop import Shop
from pages.my_account import myAccount
from pages.checkout import Checkout
import time

def test_checkout_by_admin(driver, variables):
    my_account_page = myAccount(driver, variables['url'] + 'my-account').open()
    login = myAccount(driver, variables)
    login.authorize(variables)
    shop_page = Shop(driver, variables['url'] + 'shop').open()
    addproduct = Shop(driver, variables)
    addproduct.buy_product()
    checkout_page = Checkout(driver, variables['url'] + 'checkout').open()
    time.sleep(20)
    # checkout = Checkout(driver, variables)
    # assert checkout.check_products_in_cart == True
    # checkout.fill_billing_details()
    # checkout.fill_payment_details()
    # checkout.fill_terms()
    # checkout.place_order()