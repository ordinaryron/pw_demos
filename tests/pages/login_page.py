import os
from dotenv import load_dotenv
from playwright.sync_api import Page, Response

load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.secure_alert_banner = page.get_by_label("You logged out of the secure area!")
        self.bad_username_password_banner = page.locator("#flash")
        self.heading = page.get_by_role("heading", level=1)
        self.username_label = page.get_by_label("Username")
        self.password_label = page.get_by_label("Password")
        self.input_username = page.locator("#username")
        self.input_password = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self) -> Response:
            return self.page.goto("/login")
    
    def login_good_credentials(self):
        username = os.getenv("TEST_USERNAME")
        password = os.getenv("TEST_PASSWORD")

        #Make sure these values exist
        if not username:
            raise ValueError("Missing TEST_USERNAME environment variable")
        if not password:
            raise ValueError("Missing TEST_PASSWORD environment variable")
        
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.login_button.click()

    def login_bad_username(self):
        username = "bad_username"
        password = os.getenv("TEST_PASSWORD")

        self.input_username.fill(username)
        self.input_password.fill(password)
        self.login_button.click()

    def login_bad_password(self):
        username = os.getenv("TEST_USERNAME")
        password = "bad_password"
    
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.login_button.click()