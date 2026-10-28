from playwright.sync_api import Page, Response

class OneTimePasswordPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.email_label = page.get_by_label("Your Email Address")
        self.input_email = page.locator("#email")
        self.submit_button = page.get_by_role("button", name="Send OTP Code")
        self.error_message = page.get_by_text("Please enter a valid email address.")

    def navigate(self) -> Response:
        return self.page.goto("/otp-login")

    def send_otp_code(self):
        valid_email = "practice@expandtesting.com"
        self.input_email.fill(valid_email)
        self.submit_button.click()