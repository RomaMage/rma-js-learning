import uuid
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

small_wait = 20

# Manipulate with html elements functions
def wait_for_element_visible(self, selector):
    element = WebDriverWait(self, small_wait).until(EC.visibility_of_element_located(selector))
    return element

def wait_for_element_clickable(self, selector):
    element = WebDriverWait(self, small_wait).until(EC.element_to_be_clickable(selector))
    return element

# Generate unique values names and emails
def unique_email():
    unique_email = (uuid.uuid4().hex + '@endc.com')
    shorten_email = str(unique_email)[20:]
    return shorten_email

def unique_name():
    unique_name = (uuid.uuid4().hex)
    shorten_name = str('Test' + (unique_name)[20:])
    return shorten_name

def scroll_to_element(self, selector):
    element = self.driver.find_element_by_css_selector(selector)
    actions = AC(self.driver)
    actions.move_to_element(element).perform()

# Close some banners and chats functions
def close_chat(driver):
    _chat_frame_selector_ = 'div.zopim > iframe'
    _chat_minimize_locator_ = (By.CSS_SELECTOR, ('.meshim_widget_widgets_titleBar_MinimizeButton'))

    driver.switch_to.frame(driver.find_elements_by_css_selector(_chat_frame_selector_)[1])
    elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located(_chat_minimize_locator_))
    elements[0].click()
    driver.switch_to.default_content()

def close_gdpr_banner(self):
    _gdpr_window_close_locator_ = (By.CSS_SELECTOR, '.gdpr-modal-notify span.btn-close')

    time.sleep(5)
    wait_for_element_clickable(self, _gdpr_window_close_locator_).click()

def start_testing(driver, variables):
    time.sleep(5)
    driver.get(variables['url'])
    close_gdpr_banner(driver)
    close_chat(driver)