from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from pages.utils import utils

class TestProjectPageModel:
    """
    Класс для моделирования страницы проекта с использованием Selenium WebDriver.
    Предоставляет методы для взаимодействия с селекторами типа проекта и полем ввода названия проекта.
    """

    def setup_class(self, driver, needed_project_type_name: str = "Internal", needed_project_name: str = "Привет"):
        """
        Инициализирует класс с предоставленным WebDriver и деталями проекта.

        :param driver: Экземпляр Selenium WebDriver.
        :param needed_project_type_name: Название необходимого типа проекта (по умолчанию "Internal").
        :param needed_project_name: Название необходимого проекта (по умолчанию "Привет").
        :return: self
        """
        self.driver = driver
        self.header = (By.CSS_SELECTOR, ".mIOwrtWBkxKTBAoCIb0g")
        self.needed_project_type_name = needed_project_type_name
        self.needed_project_name = needed_project_name

        self.project_type_selector = (By.CSS_SELECTOR, "#react-select-2--value input")
        self.project_type_menu_outer = (By.CSS_SELECTOR, ".Select-menu-outer")
        self.project_name_input = (By.CSS_SELECTOR, ".L40Ce1dkZzDwkTX8jmo3")
        self.selected_value_input = (By.CSS_SELECTOR, ".Select-value-label")

        return self

    def wait_until_loaded(self, timeout: int = 10):
        """
        Ожидает, пока элемент заголовка будет отрисован на странице.

        :param timeout: Максимальное время ожидания для загрузки элемента (по умолчанию 10 секунд).
        """
        utils.wait_until_element_render(self.driver, timeout, self.header)

    def select_project_type_selector(self):
        """
        Выбирает тип проекта, отправляя название в поле ввода селектора типа проекта.
        """
        self.driver.find_element(*self.project_type_selector).send_keys(self.needed_project_type_name)

    def verify_selected_project_type(self):
        """
        Проверяет, что выбранный тип проекта соответствует ожидаемому типу проекта.

        :raises AssertionError: Если выбранный тип проекта не соответствует ожидаемому названию.
        """
        if self.driver.find_element(*self.selected_value_input).text.strip() != self.needed_project_type_name:
            assert False, "Неправильный тип проекта выбран"

    def click_outer_project_type(self):
        """
        Кликает на внешний меню типа проекта для отображения доступных опций.
        """
        self.driver.find_element(*self.project_type_menu_outer).click()

    def write_project_name(self):
        """
        Записывает указанное название проекта в поле ввода названия проекта.
        """
        self.driver.find_element(*self.project_name_input).send_keys(self.needed_project_name)

    def verify_project_name(self):
        """
        Проверяет, что введенное название проекта соответствует ожидаемому названию.

        :raises AssertionError: Если введенное название проекта не соответствует ожидаемому названию.
        """
        if self.driver.find_element(*self.project_name_input).get_attribute('value').strip() != self.needed_project_name:
            assert False, "Неправильное название проекта"