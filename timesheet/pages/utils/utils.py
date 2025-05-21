import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def wait_until_element_render(driver, timeout, element):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(element)
        )
        time.sleep(1)
        assert True
    except (NoSuchElementException, AssertionError):
        assert False, f"Waiting failed: Element {element} not found."
