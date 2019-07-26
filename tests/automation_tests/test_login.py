from commands import *
from pages.my_account import myAccount
import time

# Test New User Registration
def test_register_new_user(driver, variables):
    start_testing(driver, variables)
    register = myAccount(driver, variables)
    register.register_new_user(driver, variables)
    assert register.check_if_logged() == True

# Test Login
def test_login(driver, variables):
    start_testing(driver, variables)
    login = myAccount(driver, variables)
    login.login_user(driver, variables)
    assert login.check_if_logged() == True