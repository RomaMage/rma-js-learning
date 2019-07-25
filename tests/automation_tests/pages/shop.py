from commands import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pypom import Page

class Shop(Page):
    # Elements by Selector on page

    _first_product_buy_item_locator_ = (By.CSS_SELECTOR, 'ul.products li:first-child a.add_to_cart_button')

    def buy_product(self):
        wait_for_element_clickable(self, self._first_product_buy_item_locator_).click()