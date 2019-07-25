import uuid
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

small_wait = 20

def wait_for_element_visible(self, selector):
    element = WebDriverWait(self, small_wait).until(EC.visibility_of_element_located(selector))
    return element

def wait_for_element_clickable(self, selector):
    element = WebDriverWait(self, small_wait).until(EC.element_to_be_clickable(selector))
    return element

def unique_email():
    unique_email = (uuid.uuid4().hex + '@endc.com')
    shorten_email = str(unique_email)[20:]
    return shorten_email

def unique_name():
    unique_name = (uuid.uuid4().hex)
    shorten_name = str('Test' + (unique_name)[20:])
    return shorten_name