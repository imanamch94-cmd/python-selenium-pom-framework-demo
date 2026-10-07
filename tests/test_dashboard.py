from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_dashboard_regression(driver):
    LoginPage(driver).login("ankhan@cinnova.com", "Testing1234")
    time.sleep(5)
    dash = DashboardPage(driver)
    sidebar = dash.get_sidebar_items()
    print(f"SIDEBAR FOUND: {sidebar}")
    assert len(sidebar) >= 5
    driver.save_screenshot("final_agtown_pass.png")
    print("✅ DASHBOARD REGRESSION PASS")