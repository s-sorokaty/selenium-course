from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.utils import utils


class TestTimeTrackerPageModel:
    """
    Класс для представления модели страницы трекера времени для целей тестирования.

    Атрибуты:
        driver: Экземпляр WebDriver, используемый для взаимодействия с браузером.
        add_activity_link: Локатор для ссылки добавления активности.
        submit_activity_button: Локатор для кнопки отправки активности.
        add_modal_link: Локатор для ссылки открытия модального окна добавления проекта.
        task_element: Лямбда-функция для получения локатора элемента задачи по имени задачи.
        days_time_elements: Локатор для элементов ввода времени по дням.
    """

    def setup_class(self, driver):
        """
        Инициализирует класс TestTimeTrackerPageModel с экземпляром WebDriver.

        Аргументы:
            driver: Экземпляр WebDriver для управления браузером.
        
        Возвращает:
            self: Экземпляр класса TestTimeTrackerPageModel.
        """
        self.driver = driver
        self.add_activity_link = (By.CSS_SELECTOR, ".iBGlMfnpJsnZWrdgnW8p.addActivity")
        self.submit_activity_button = (By.CSS_SELECTOR, ".Ej2j7rcVLbhJz0ZdXwwp.ZDmpprui3jNJxbhP4qL2")
        self.add_modal_link = (By.CSS_SELECTOR, ".addProject>button")
        self.task_element = lambda task_name: (By.XPATH, f"/html/body/*/div/div/div/form/*/*/div/span/div/div/table/tbody/*/*[contains(text(),'{task_name}')]")
        self.days_time_elements = (By.CSS_SELECTOR, ".JwTdWUOJwtyX29O3FwKW.taskRow>td input")

        return self
    
    def wait_until_loaded(self, timeout:int=10):
        """
        Ожидает, пока ссылка добавления активности не будет отображена на странице.

        Аргументы:
            timeout: Максимальное время ожидания загрузки элемента (по умолчанию 10 секунд).
        """
        utils.wait_until_element_render(self.driver, timeout, self.add_activity_link)

    def click_activity(self):
        """
        Нажимает на ссылку добавления активности.
        """
        self.driver.find_element(*self.add_activity_link).click()

    def check_modal_opened(self, timeout:int=10):
        """
        Ожидает, пока модальное окно добавления проекта не будет открыто.

        Аргументы:
            timeout: Максимальное время ожидания загрузки элемента (по умолчанию 10 секунд).
        """
        utils.wait_until_element_render(self.driver, timeout, self.add_modal_link)

    def select_task_to_fill(self, task_name:str):
        """
        Выбирает задачу для заполнения по имени задачи.

        Аргументы:
            task_name: Имя задачи, которую нужно выбрать.
        """
        self.driver.find_element(*self.task_element(task_name)).click()

    def click_modal(self):
        """
        Нажимает на кнопку для открытия модального окна добавления проекта.
        """
        self.driver.find_element(*self.add_modal_link).click()
    
    def fill_days(self, time_array:list[int]=None):
        """
        Заполняет поля ввода времени по дням.

        Аргументы:
            time_array: Список значений времени для заполнения (по умолчанию [8, 8, 8, 8, 8, 0, 0]).
        """
        if time_array is None: 
            time_array = [8, 8, 8, 8, 8, 0, 0]
        for i, element in enumerate(self.driver.find_elements(*self.days_time_elements)):
            element.clear()
            element.send_keys(str(time_array[i]))
    
    def submit_activity(self):
        """
        Нажимает на кнопку отправки активности.
        """
        self.driver.find_element(*self.submit_activity_button).click()
