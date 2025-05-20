import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class TestProjectPageModel:
    
    def setup_class(self, driver, needed_project_type_name:str="Internal", needed_project_name:str="Привет"):
        self.driver = driver
        self.header = (By.CSS_SELECTOR, ".mIOwrtWBkxKTBAoCIb0g")
        self.needed_project_type_name = needed_project_type_name
        self.needed_project_name = needed_project_name

        self.project_type_selector = (By.CSS_SELECTOR, "#react-select-2--value input")
        self.project_type_menu_outer = (By.CSS_SELECTOR, ".Select-menu-outer")
        self.project_name_input = (By.CSS_SELECTOR, ".L40Ce1dkZzDwkTX8jmo3")
        self.selected_value_input = (By.CSS_SELECTOR , ".Select-value-label")
        
        return self
    
    def wait_until_loaded(self, timeout:int=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.header)
            )
            assert True
        except (NoSuchElementException, AssertionError):
            assert False, "Page loading failed: Element not found."

    def select_project_type_selector(self,):
        self.driver.find_element(*self.project_type_selector).send_keys(self.needed_project_type_name)

    def verify_selected_project_type(self,):
        try:
            if self.driver.find_element(*self.selected_value_input).text.strip() != self.needed_project_type_name: 
                assert False, "Wrong type selected"
        except NoSuchElementException:
            assert False, "Selected element not found."

    def click_outer_project_type(self,):
        self.driver.find_element(*self.project_type_menu_outer).click()
    
    def write_project_name(self,):
        self.driver.find_element(*self.project_name_input).send_keys(self.needed_project_name)
    
    def verify_project_name(self,):
        try:
            if self.driver.find_element(*self.project_name_input).get_attribute('value').strip() != self.needed_project_name: 
                assert False, "Wrong project name"
        except NoSuchElementException:
            assert False, "Selected element not found."