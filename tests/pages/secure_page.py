from playwright.sync_api import Page, Response

class SecurePage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.secure_text = page.get_by_text("Welcome to the Secure Area. When you are done click logout below.")
        self.greeting_text = page.get_by_text("Hi, ")
        self.secure_alert_banner = page.locator("#flash")

        # The logout button is a trick because it's not a button, it's a link that looks like a button.
        self.logout_button = page.get_by_role("link", name="Logout")
        
    def logout(self):
        self.logout_button.click()