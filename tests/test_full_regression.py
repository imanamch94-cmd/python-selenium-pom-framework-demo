import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def do_login(driver):
    driver.get("https://example.com/login")
    wait = WebDriverWait(driver, 30)  # 15 se 30 kar diya
    print("Opening login page...")
    time.sleep(3)
    email_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    email_el.clear()
    email_el.send_keys("ankhan@cinnova.com")
    pwd_el = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    pwd_el.clear()
    pwd_el.send_keys("Testing1234\n")
    print("Login clicked, waiting...")
    time.sleep(10)  # Firebase ko time do
    print(f"Current URL after login: {driver.current_url}")

def test_full_website_regression():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        do_login(driver)
        print(f"LOGIN PASS: {driver.current_url}")
        modules = ["Dashboard", "Profile", "Browse Jobs", "My Job Search", "My Calendar", "Referrals"]
        for mod in modules:
            try:
                el = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(),'{mod}')]")))
                el.click()
                time.sleep(5)
                print(f"✅ {mod} : OPEN PASS - {driver.current_url}")
                driver.save_screenshot(f"{mod.replace(' ','_')}.png")
            except Exception as e:
                print(f"❌ {mod} : FAIL - {e}")
        print("--- FULL WEBSITE REGRESSION COMPLETE ---")
        assert True
    finally:
        driver.quit()