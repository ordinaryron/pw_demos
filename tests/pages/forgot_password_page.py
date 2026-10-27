from playwright.sync_api import Page, Response

class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.email_label = page.get_by_text("E-mail", exact=True)
        self.email_input = page.locator("#email")
        self.email_button = page.get_by_role("button", name="Retrieve password")
        self.error_text = page.get_by_text("Please enter a valid email address.")

    def navigate(self) -> Response:
        return self.page.goto("/forgot-password")

    def submit_email(self):
        self.email_input.fill("dummyemail@dummy.com")
        self.email_button.click()