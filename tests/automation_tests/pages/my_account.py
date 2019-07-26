from commands import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pypom import Page
import time

class myAccount(Page):
    # Elements by CSS selector
    _logged_text_locator_ = (By.CSS_SELECTOR, '.woocommerce-MyAccount-content p')

    # Login Form Elements
    _email_field_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-login #username')
    _password_field_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-login #password')
    _login_submit_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-login .woocommerce-form-login__submit')

    # Register form Elements
    _reg_email_address_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register #reg_email')
    _reg_password_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register #reg_password')
    _reg_password_confirm_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register #reg_password_confirm')
    _reg_first_name_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register #first_name')
    _reg_last_name_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register #last_name')
    _reg_register_submit_locator_ = (By.CSS_SELECTOR, '.woocommerce-form-register .woocommerce-Button')

    # Chat elements
    _chat_frame_locator_ = 'div.zopim > iframe'
    _chat_minimize_locator_ = (By.CSS_SELECTOR, ('.meshim_widget_widgets_titleBar_MinimizeButton'))
        
    def check_if_logged(self):
        logged_text = wait_for_element_visible(self, self._logged_text_locator_).text
        flag = logged_text.find('Hello')
        if flag >= 0:
            return True
        else :
            return False

    def authorize(self, variables):
        wait_for_element_visible(self, self._email_field_locator_).send_keys(variables['admin_email'])
        wait_for_element_visible(self, self._password_field_locator_).send_keys(variables['admin_pass'])
        wait_for_element_clickable(self, self._login_submit_locator_).click()

    def fill_register_data(self, variables):
        wait_for_element_visible(self, self._reg_email_address_locator_).send_keys(unique_email())
        wait_for_element_visible(self, self._reg_password_locator_).send_keys(variables['pass'])
        wait_for_element_visible(self, self._reg_password_confirm_locator_).send_keys(variables['pass'])
        wait_for_element_visible(self, self._reg_first_name_locator_).send_keys(unique_name())
        wait_for_element_visible(self, self._reg_last_name_locator_).send_keys(variables['last_name'])

    def register_new_user(self, driver, variables):
        driver.get(variables['url'] + 'my-account')
        self.fill_register_data(variables)
        wait_for_element_clickable(self, self._reg_register_submit_locator_).click()

    def login_user(self, driver, variables):
        driver.get(variables['url'] + 'my-account')
        self.authorize(variables)