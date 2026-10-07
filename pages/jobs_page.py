from selenium.webdriver.common.by import By
import time

class JobsPage:
    def __init__(self, driver):
        self.driver = driver

    def validate(self):
        time.sleep(4)
        cards = self.driver.find_elements(By.XPATH, "//*[contains(@class,'job') or contains(@class,'card') or contains(text(),'Apply')]")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        return {"jobs_or_cards": len(cards), "buttons": len(buttons), "url": self.driver.current_url}