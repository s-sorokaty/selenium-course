import pytest
from selenium import webdriver

from config import Settings
from pages.login_page_model import TestLoginPage
from pages.tracker_page_model import TestTimeTrackerPageModel
from pages.project_page_model import TestProjectPageModel


class TestMain:
    """
    Класс для проведения тестов на главной странице приложения.

    Методы:
        driver: Фикстура для создания и управления экземпляром WebDriver.
        test_login: Тест для проверки процесса входа в систему.
        test_open_project: Тест для открытия страницы проекта.
        test_project_page: Тест для проверки функциональности страницы проекта.
        test_open_tracker: Тест для открытия страницы трекера времени.
        test_fill_in_tracker: Тест для заполнения трекера времени.
        test_fill_out_tracker: Тест для обнуления трекера времени.
    """

    @pytest.fixture(scope="class")
    def driver(self):
        """
        Фикстура для создания экземпляра WebDriver.

        Возвращает:
            driver: Экземпляр WebDriver для управления браузером.
        """
        driver = webdriver.Chrome()  
        yield driver
        driver.quit()

    def test_login(self, driver):
        """
        Тест для проверки процесса входа в систему.

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        """
        driver.get("http://track.nordclan/login")  
        login_page = TestLoginPage().setup_class(driver)

        login_page.wait_until_loaded(5)
        login_page.enter_username(Settings().TRACKER_USERNAME)
        login_page.enter_password(Settings().TRACKER_PASSWORD)
        login_page.click_login()
        login_page.wait_verify_login(5)
    
    @pytest.mark.skip    
    def test_open_project(self, driver):
        """
        Тест для открытия страницы проекта (пропущен).

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        
        Возвращает:
            project_page: Экземпляр модели страницы проекта.
        """
        driver.get("http://track.nordclan/projects")  
        project_page = TestProjectPageModel().setup_class(driver)
        project_page.wait_until_loaded(5)
        return project_page
    
    def test_project_page(self, driver):
        """
        Тест для проверки функциональности страницы проекта.

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        """
        project_page = self.test_open_project(driver)

        project_page.select_project_type_selector()
        project_page.click_outer_project_type()
        project_page.verify_selected_project_type()
        project_page.write_project_name()
        project_page.verify_project_name()

    @pytest.mark.skip    
    def test_open_tracker(self, driver):
        """
        Тест для открытия страницы трекера времени (пропущен).

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        
        Возвращает:
            tracker_page: Экземпляр модели страницы трекера времени.
        """
        driver.get("http://track.nordclan/timereports")  
        tracker_page = TestTimeTrackerPageModel().setup_class(driver)
        tracker_page.wait_until_loaded(5)
        return tracker_page
    
    @pytest.mark.skip    
    def test_fill_in_tracker(self, driver):
        """
        Тест для заполнения трекера времени (пропущен).

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        """
        tracker_page = self.test_open_tracker(driver)

        tracker_page.click_activity()
        tracker_page.check_modal_opened(5)
        tracker_page.select_task_to_fill("Подготовка к интервью")
        tracker_page.click_modal()
        tracker_page.fill_days()
        # tracker_page.submit_activity_button()
        
    @pytest.mark.skip    
    def test_fill_out_tracker(self, driver):
        """
        Тест для обнуления трекера времени (пропущен).

        Аргументы:
            driver: Экземпляр WebDriver, используемый для доступа к веб-странице.
        """
        tracker_page = self.test_open_tracker(driver)

        tracker_page.click_activity()
        tracker_page.check_modal_opened(5)
        tracker_page.select_task_to_fill("Подготовка к интервью")
        tracker_page.click_modal()
        tracker_page.fill_days([0 for _ in range(0, 9)])