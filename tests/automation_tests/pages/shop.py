from commands import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pypom import Page
import time

class Shop(Page):

    # Buy product locator
    _first_product_buy_item_locator_ = (By.CSS_SELECTOR, 'ul.products li.first:first-child a.ajax_add_to_cart')

    def buy_product(self, driver, variables):
        driver.get(variables['url'] + 'shop/cbd-oil')
        time.sleep(2)
        wait_for_element_clickable(self, self._first_product_buy_item_locator_).click()
        time.sleep(3)