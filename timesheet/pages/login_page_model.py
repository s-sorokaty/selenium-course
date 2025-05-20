from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage:
    
    def setup_class(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, ".VEk5WthgxYcIVhuIU03A>form>.EJuttC7wKjeJSPjMDXYC:nth-child(1)>.TLXEsbTRcoKoM0vjy_oM>input")
        self.password_input = (By.CSS_SELECTOR, ".VEk5WthgxYcIVhuIU03A>form>.EJuttC7wKjeJSPjMDXYC:nth-child(2)>.TLXEsbTRcoKoM0vjy_oM>input")
        self.login_button = (By.CSS_SELECTOR, ".qGLZALY5nme1UW33jLFw>button")
        self.verify_block = (By.CSS_SELECTOR, ".iVAjU68E5AMyxvlTI3ql")

        return self
    
    def wait_until_loaded(self, timeout:int=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.username_input)
            )
            assert True
        except (NoSuchElementException, AssertionError):
            assert False, "Login failed: Element not found."

    def enter_username(self, username:str):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password:str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def wait_verify_login(self, timeout:int=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.verify_block)
            )
            assert True
        except (NoSuchElementException, AssertionError):
            assert False, "Login verification failed: Element not found."