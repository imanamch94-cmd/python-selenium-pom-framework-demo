from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.jobs_page import JobsPage
import time

def test_browse_jobs_regression(driver):
    LoginPage(driver).login("ankhan@cinnova.com", "Testing1234")
    time.sleep(6)
    DashboardPage(driver).go_to("Browse Jobs")
    info = JobsPage(driver).validate()
    print(f"BROWSE JOBS: {info}")
    driver.save_screenshot("browse_jobs.png")
    assert info["buttons"] > 0
    print("✅ BROWSE JOBS PASS")