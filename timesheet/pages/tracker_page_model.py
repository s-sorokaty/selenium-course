import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class TestTimeTrackerPageModel:
    
    def setup_class(self, driver):
        self.driver = driver
        self.add_activity_link = (By.CSS_SELECTOR, ".iBGlMfnpJsnZWrdgnW8p.addActivity")
        self.submit_activity_button = (By.CSS_SELECTOR, ".Ej2j7rcVLbhJz0ZdXwwp.ZDmpprui3jNJxbhP4qL2")
        self.add_modal_link = (By.CSS_SELECTOR, ".addProject>button")
        self.task_element = lambda task_name:(By.XPATH, f"/html/body/*/div/div/div/form/*/*/div/span/div/div/table/tbody/*/*[contains(text(),'{task_name}')]") 
        self.days_time_elements = (By.CSS_SELECTOR, ".JwTdWUOJwtyX29O3FwKW.taskRow>td input")

        #f"//*[@id='app']/div/*/div/*/*/div/div/section/table/tbody/*[contains(text(),'{task_name}')]"
        return self
    
    def wait_until_loaded(self, timeout:int=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.add_activity_link)
            )
            assert True
        except (NoSuchElementException, AssertionError):
            assert False, "Page loading failed: Element not found."

    def click_activity(self):
        self.driver.find_element(*self.add_activity_link).click()

    def check_modal_opened(self, timeout:int=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.add_modal_link)
            )
            time.sleep(1)
        except (NoSuchElementException, AssertionError):
            assert False, "Cannot open modal: Element not found."

    def select_task_to_fill(self, task_name:str):
        self.driver.find_element(*self.task_element(task_name)).click()

    def click_modal(self,):
        self.driver.find_element(*self.add_modal_link).click()
    
    def fill_days(self, time_array:list[int]=None):
        if time_array is None: time_array = [8,8,8,8,8,0,0]
        for i, element in enumerate(self.driver.find_elements(*self.days_time_elements)):
            element.clear()
            element.send_keys(str(time_array[i]))
    
    def submit_activity(self,):
        self.driver.find_element(*self.submit_activity_button).click()