import time
import pytest
from selenium import webdriver

from config import Settings
from pages.login_page_model import TestLoginPage
from pages.tracker_page_model import TestTimeTrackerPageModel
from pages.project_page_model import TestProjectPageModel


class TestMain:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()  
        yield driver
        driver.quit()

    def test_login(self, driver):
        driver.get("http://track.nordclan/login")  
        login_page = TestLoginPage().setup_class(driver)

        login_page.wait_until_loaded(5)
        login_page.enter_username(Settings().TRACKER_USERNAME)
        login_page.enter_password(Settings().TRACKER_PASSWORD)
        login_page.click_login()
        login_page.wait_verify_login(5)
    
    @pytest.mark.skip    
    def test_open_project(self, driver):
        driver.get("http://track.nordclan/projects")  
        project_page = TestProjectPageModel().setup_class(driver)
        project_page.wait_until_loaded(5)
        return project_page
    
    def test_project_page(self, driver):
        project_page = self.test_open_project(driver)

        project_page.select_project_type_selector()
        project_page.click_outer_project_type()
        project_page.verify_selected_project_type()
        project_page.write_project_name()
        project_page.verify_project_name()

    @pytest.mark.skip    
    def test_open_tracker(self, driver):
        driver.get("http://track.nordclan/timereports")  
        tracker_page = TestTimeTrackerPageModel().setup_class(driver)
        tracker_page.wait_until_loaded(5)
        return tracker_page
    
    @pytest.mark.skip    
    def test_fill_in_tracker(self, driver):
        tracker_page = self.test_open_tracker(driver)

        tracker_page.click_activity()
        tracker_page.check_modal_opened(5)
        tracker_page.select_task_to_fill("Подготовка к интервью")
        tracker_page.click_modal()
        tracker_page.fill_days()
        #tracker_page.submit_activity_button()
        
        
    @pytest.mark.skip    
    def test_fill_out_tracker(self, driver):
        tracker_page = self.test_open_tracker(driver)

        tracker_page.click_activity()
        tracker_page.check_modal_opened(5)
        tracker_page.select_task_to_fill("Подготовка к интервью")
        tracker_page.click_modal()
        tracker_page.fill_days([0 for _ in range(0,9)])
        
