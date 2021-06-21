from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class IllegalStateError(Exception):
    pass


class LoginPage:
    def __init__(self, driver, url, user_locator, password_locator, login_locator):
        self.driver = driver
        self.driver.get(url)
        self.username_field = self.driver.find_element(*user_locator)
        self.password_field = self.driver.find_element(*password_locator)
        self.login_button = self.driver.find_element(*login_locator)

    def login(self, name, password):
        self.username_field.send_keys(name)
        self.password_field.send_keys(password)
        self.login_button.click()


class HomePage:
    def __init__(self, driver, user_name, name_locator):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)
        name_label = self.wait.until(EC.presence_of_element_located(name_locator))
        if user_name != name_label.text:
            raise IllegalStateError("This is not Home Page")

    def click(self, frame_locator, btn_locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
        element = self.wait.until(EC.presence_of_element_located(btn_locator))
        element.click()
