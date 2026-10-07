from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_sidebar_items(self):
        items = ["Dashboard", "Profile", "Browse Jobs", "My Job Search", "My Calendar", "Referrals"]
        found = []
        for item in items:
            if self.driver.find_elements(By.XPATH, f"//*[contains(text(),'{item}')]"):
                found.append(item)
        return found

    def go_to(self, menu_text):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(),'{menu_text}')]")))
        el.click()
        time.sleep(3)