from commands import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pypom import Page
import time

class Checkout(Page):
    # Elements on Checkout Page

    # Billing Details Fields
    _billing_first_name_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_first_name'))
    _billing_last_name_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_last_name'))
    _billing_street_address_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_address_1'))
    _billing_city_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_city'))
    _billing_state_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_state'))
    _billing_postcode_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_postcode'))
    _billing_phone_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_phone'))
    _billing_email_locator_ = (By.CSS_SELECTOR, ('.woocommerce-checkout #billing_email'))

    # Payment method 
    _payment_method_locator_ = (By.CSS_SELECTOR, ('#payment #payment_method_bacs'))

    # Terms checkbox
    _terms_checkbox_locator_ = (By.CSS_SELECTOR, ('.woocommerce-terms-and-conditions-wrapper #terms'))

    _place_order_locator_ = (By.CSS_SELECTOR, ('button#place_order'))

    # Order Details
    _order_details_title_locator_ = (By.CSS_SELECTOR, ('h2.woocommerce-order-details__title'))
        

    # Fill Checkout Billing Details
    def fill_billing_details(self):
        # Fill fields
        wait_for_element_visible(self, self._billing_first_name_locator_).clear()
        wait_for_element_visible(self, self._billing_first_name_locator_).send_keys('Test Customer')
        wait_for_element_visible(self, self._billing_last_name_locator_).clear()
        wait_for_element_visible(self, self._billing_last_name_locator_).send_keys('Auto Test Customer')
        wait_for_element_visible(self, self._billing_street_address_locator_).clear()
        wait_for_element_visible(self, self._billing_street_address_locator_).send_keys('Gagarina str 1')
        wait_for_element_visible(self, self._billing_city_locator_).clear()
        wait_for_element_visible(self, self._billing_city_locator_).send_keys('Boston')
        wait_for_element_visible(self, self._billing_state_locator_).clear()
        wait_for_element_visible(self, self._billing_state_locator_).send_keys('California')
        wait_for_element_visible(self, self._billing_postcode_locator_).clear()
        wait_for_element_visible(self, self._billing_postcode_locator_).send_keys('127879')
        wait_for_element_visible(self, self._billing_phone_locator_).clear()
        wait_for_element_visible(self, self._billing_phone_locator_).send_keys('+29321234567')
        wait_for_element_visible(self, self._billing_email_locator_).clear()
        wait_for_element_visible(self, self._billing_email_locator_).send_keys('test.customer@mail.com')
        time.sleep(5)

    # Fill Payment Details
    def fill_payment_details(self):
        wait_for_element_clickable(self, self._payment_method_locator_).click()
        time.sleep(2)

    # Check Terms checkbox
    def fill_terms(self):
        wait_for_element_clickable(self, self._terms_checkbox_locator_).click()

    # Place Order
    def place_order(self):
        scroll_to_element(self, '.cta_container')
        wait_for_element_clickable(self, self._place_order_locator_).click()
        time.sleep(10)
    
    def fill_checkout(self, driver, variables):
        driver.get(variables['url'] + 'checkout')
        self.fill_billing_details()
        self.fill_payment_details()
        self.fill_terms()
        self.place_order()

    #Check if order placed correctly
    def check_order_details(self):
        time.sleep(5)
        order_text = wait_for_element_visible(self, self._order_details_title_locator_).text
        flag = order_text.find('Order')
        if flag >= 0 :
            return True
        else :
            return False