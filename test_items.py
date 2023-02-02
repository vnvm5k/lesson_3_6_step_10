from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_button(browser):

	browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

	time.sleep(12)

	button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

	assert len(button) > 0, "Button is not found"