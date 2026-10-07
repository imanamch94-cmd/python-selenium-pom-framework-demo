from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.email = (By.CSS_SELECTOR, "input[type='email']")
        self.password = (By.CSS_SELECTOR, "input[type='password']")

    def open(self):
        self.driver.get("https://example.com/login")

    def login(self, email, pwd):
        self.open()
        self.wait.until(EC.presence_of_element_located(self.email)).send_keys(email)
        self.driver.find_element(*self.password).send_keys(pwd + "\n")
        self.wait.until(lambda d: "login" not in d.current_url.lower())