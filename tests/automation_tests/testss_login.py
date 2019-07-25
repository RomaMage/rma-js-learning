from commands import *
from pages.my_account import myAccount
import time

# Test New User Registration
def test_register_new_user(driver, variables):
    my_account_page = myAccount(driver, variables['url'] + 'my-account').open()
    register = myAccount(driver, variables)
    register.register_new_user(variables)
    assert register.check_if_logged() == True

# Test Login
def test_login(driver, variables):
    my_account_page = myAccount(driver, variables['url'] + 'my-account').open()
    login = myAccount(driver, variables)
    login.authorize(variables)
    assert login.check_if_logged() == True