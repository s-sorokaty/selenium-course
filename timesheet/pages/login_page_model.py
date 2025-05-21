from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from pages.utils import utils


class TestLoginPage:
    """
    Класс для представления страницы входа для целей тестирования.

    Атрибуты:
        driver: Экземпляр WebDriver, используемый для взаимодействия с браузером.
        username_input: Локатор для поля ввода имени пользователя.
        password_input: Локатор для поля ввода пароля.
        login_button: Локатор для кнопки входа.
        verify_block: Локатор блока, который проверяет успешный вход.
    """

    def setup_class(self, driver):
        """
        Инициализирует класс TestLoginPage с экземпляром WebDriver.

        Аргументы:
            driver: Экземпляр WebDriver для управления браузером.
        
        Возвращает:
            self: Экземпляр класса TestLoginPage.
        """
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, ".VEk5WthgxYcIVhuIU03A>form>.EJuttC7wKjeJSPjMDXYC:nth-child(1)>.TLXEsbTRcoKoM0vjy_oM>input")
        self.password_input = (By.CSS_SELECTOR, ".VEk5WthgxYcIVhuIU03A>form>.EJuttC7wKjeJSPjMDXYC:nth-child(2)>.TLXEsbTRcoKoM0vjy_oM>input")
        self.login_button = (By.CSS_SELECTOR, ".qGLZALY5nme1UW33jLFw>button")
        self.verify_block = (By.CSS_SELECTOR, ".iVAjU68E5AMyxvlTI3ql")

        return self
    
    def wait_until_loaded(self, timeout:int=10):
        """
        Ожидает, пока поле ввода имени пользователя не будет отображено на странице.

        Аргументы:
            timeout: Максимальное время ожидания загрузки элемента (по умолчанию 10 секунд).
        """
        utils.wait_until_element_render(self.driver, timeout, self.username_input)

    def enter_username(self, username:str):
        """
        Вводит имя пользователя в поле ввода имени пользователя.

        Аргументы:
            username: Имя пользователя, которое нужно ввести.
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password:str):
        """
        Вводит пароль в поле ввода пароля.

        Аргументы:
            password: Пароль, который нужно ввести.
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """
        Нажимает на кнопку входа для отправки формы входа.
        """
        self.driver.find_element(*self.login_button).click()

    def wait_verify_login(self, timeout:int=10):
        """
        Ожидает, пока блок проверки не будет отображен, что указывает на успешный вход.

        Аргументы:
            timeout: Максимальное время ожидания загрузки блока проверки (по умолчанию 10 секунд).
        """
        utils.wait_until_element_render(self.driver, timeout, self.verify_block)